from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
# tf.enable_eager_execution() Necessary in Tensorflow 1.X
import numpy as np
import os

class NLP:


    def __init__(self):
        print("> NLP initialized")

    """
        Spliting to training and labeling sets (X,Y)
        @:returns X,Y
    """
    def splitXY(self,chunk):
        input_text = chunk[:-1]
        target_text = chunk[1:]
        return input_text, target_text

    """
        Loss function to use while training
    """
    def loss(self,labels, logits):
        return tf.keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits=True)

    """
        Creating the vocabulary and the coresponding dataset.
        Encoding input text characters to RNN readable numbers
        @:returns dataset, vocabulary
    """
    def preprocess(self, text):
        # Number of Characters in the text input
        print("Length of text: {} characters".format(len(text)))

        # Number of Unique Characters in the text input
        vocabulary = sorted(set(text))
        print('Vocabulary size: {}'.format(len(vocabulary)))

        # Mapping characters to numbers
        self.char_to_index = {u: i for i, u in enumerate(vocabulary)}
        self.index_to_char = np.array(vocabulary)
        text_as_int = np.array([self.char_to_index[c] for c in text])

        # The RNN input sequence of characters length
        seq_length = 100  # 100 characters per sentence

        # Creating Training Sets
        char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)
        sequences = char_dataset.batch(seq_length + 1, drop_remainder=True)
        dataset = sequences.map(self.splitXY)

        return dataset, vocabulary

    """
        Shuffling the dataset and preparing the model settings
        Play with these settings to improve the performance of the RNN
        @:returns dataset,vocabulary_size,embedding_dimension,rnn_nodes,batch_size 
    """
    def prepareSettings(self, dataset, vocabulary):
        # Preparing the Settings
        batch_size = 64  # Training batch per iteration
        buffer_size = 10000  # Elements in memory
        dataset = dataset.shuffle(buffer_size).batch(batch_size, drop_remainder=True)
        vocabulary_size = len(vocabulary)
        embedding_dimension = 256
        rnn_nodes = 1024  # Number of neurons in Recursive Neural Network

        return dataset, vocabulary_size, embedding_dimension, rnn_nodes, batch_size

    """
        Bulding the Deep RNN model
        NOTE:   For different datasets and scenarios I would recommend
                changing the batch_size and considering adding an additional 
                Dropout layer to improve the generalization capabilities and 
                performance of the Deep Model 
        @:returns model
    """
    def build_model(self,vocab_size, embedding_dim, rnn_units, batch_size):
        model = tf.keras.Sequential([
            tf.keras.layers.Embedding(vocab_size, embedding_dim,
                                      batch_input_shape=[batch_size, None]),
            tf.keras.layers.GRU(rnn_units,
                                return_sequences=True,
                                stateful=True,
                                recurrent_initializer='glorot_uniform'),
            tf.keras.layers.Dense(vocab_size)
        ])
        return model

    """
        Defining training callbacks (Checkpoints here) and training the model
        After each epoch the weights of the RNN are stored in a file (only if
        the loss has decreased)
    """
    def trainModel(self, dataset, model, checkpoint_dir, n_epochs):
        checkpoint_loc = os.path.join(checkpoint_dir, 'checkpoint_{epoch}')

        checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
            verbose=1,
            monitor='loss',
            filepath=checkpoint_loc,
            save_best_only=True,
            save_weights_only=True
        )

        #model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))  # Pickup Training from last checkpoint
        model.compile(optimizer='adam', loss=self.loss)
        model.fit(dataset, epochs=n_epochs, callbacks=[checkpoint_callback])

    """
        Generating new text (one character at a time) based on an initial seed.
        We make use of the latest checkpoint of the trained Deep RNN model
    """
    def generate_text(self,vocab_size, embedding_dim, rnn_units,checkpoint_dir, start_string):
        tf.train.latest_checkpoint(checkpoint_dir)
        model = self.build_model(vocab_size, embedding_dim, rnn_units, batch_size=1)

        model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))
        model.build(tf.TensorShape([1, None]))

        # Number of characters to generate
        num_generate = 150

        # Converting our start string to numbers (vectorizing)
        input_eval = [self.char_to_index[s] for s in start_string]
        input_eval = tf.expand_dims(input_eval, 0)

        # Empty string to store our results
        text_generated = []

        # Low temperatures results in more predictable text.
        # Higher temperatures results in more surprising text.
        # Experiment to find the best setting.
        temperature = 1.0

        # Here batch size == 1
        model.reset_states()
        for i in range(num_generate):
            predictions = model(input_eval)
            # remove the batch dimension
            predictions = tf.squeeze(predictions, 0)

            # using a categorical distribution to predict the character returned by the model
            predictions = predictions / temperature
            predicted_id = tf.random.categorical(predictions, num_samples=1)[-1, 0].numpy()

            # We pass the predicted character as the next input to the model
            # along with the previous hidden state
            input_eval = tf.expand_dims([predicted_id], 0)

            text_generated.append(self.index_to_char[predicted_id])

        return (start_string + ''.join(text_generated))