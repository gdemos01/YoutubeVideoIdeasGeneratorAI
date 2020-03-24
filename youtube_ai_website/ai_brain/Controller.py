import sys
import argparse

#from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
#tf.enable_eager_execution()

import numpy as np
import os
import time
import json
import warnings
warnings.filterwarnings("ignore")

def loss(labels, logits):
  return tf.keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits=True)


def split_input_target(chunk):
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text, target_text

def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
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

def generate_text(model, start_string):
  # Evaluation step (generating text using the learned model)

  # Number of characters to generate
  num_generate = 150

  # Converting our start string to numbers (vectorizing)
  input_eval = [char2idx[s] for s in start_string]
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
      predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()

      # We pass the predicted character as the next input to the model
      # along with the previous hidden state
      input_eval = tf.expand_dims([predicted_id], 0)

      text_generated.append(idx2char[predicted_id])

  return (start_string + ''.join(text_generated))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--train", action="store_true")
    parser.add_argument("--generate",action="store_true")
    parser.add_argument("--seed")
    args = parser.parse_args()

    text = open('titles.txt', 'rb').read().decode(encoding='utf-8')

    # length of text is the number of characters in it
    #print('Length of text: {} characters'.format(len(text)))

    # Take a look at the first 250 characters in text
    #print(text[:250])

    # The unique characters in the file
    vocab = sorted(set(text))
    #print('{} unique characters'.format(len(vocab)))

    # Creating a mapping from unique characters to indices
    char2idx = {u: i for i, u in enumerate(vocab)}
    idx2char = np.array(vocab)

    text_as_int = np.array([char2idx[c] for c in text])

    # print('{')
    # for char, _ in zip(char2idx, range(20)):
    #     print('  {:4s}: {:3d},'.format(repr(char), char2idx[char]))
    # print('  ...\n}')

    #Show how the first 13 characters from the text are mapped to integers
    #print('{} ---- characters mapped to int ---- > {}'.format(repr(text[:13]), text_as_int[:13]))

    #The maximum length sentence we want for a single input in characters
    seq_length = 100
    examples_per_epoch = len(text) // (seq_length + 1)

    # Create training examples / targets
    char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)

    # for i in char_dataset.take(5):
    #     print(idx2char[i.numpy()])

    sequences = char_dataset.batch(seq_length + 1, drop_remainder=True)

    # for item in sequences.take(5):
    #     print(repr(''.join(idx2char[item.numpy()])))

    dataset = sequences.map(split_input_target)

    # for input_example, target_example in dataset.take(1):
    #     print('Input data: ', repr(''.join(idx2char[input_example.numpy()])))
    #     print('Target data:', repr(''.join(idx2char[target_example.numpy()])))
    #
    # for i, (input_idx, target_idx) in enumerate(zip(input_example[:5], target_example[:5])):
    #     print("Step {:4d}".format(i))
    #     print("  input: {} ({:s})".format(input_idx, repr(idx2char[input_idx])))
    #     print("  expected output: {} ({:s})".format(target_idx, repr(idx2char[target_idx])))

    # Directory where the checkpoints will be saved
    checkpoint_dir = 'checkpoints'
    # Name of the checkpoint files
    checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")

    # Batch size
    BATCH_SIZE = 64

    BUFFER_SIZE = 10000

    dataset = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

    # Length of the vocabulary in chars
    vocab_size = len(vocab)

    # The embedding dimension
    embedding_dim = 256

    # Number of RNN units
    rnn_units = 1024

    if args.train:
        model = build_model(
            vocab_size=len(vocab),
            embedding_dim=embedding_dim,
            rnn_units=rnn_units,
            batch_size=BATCH_SIZE)
        print(len(vocab))

        # for input_example_batch, target_example_batch in dataset.take(1):
        #     example_batch_predictions = model(input_example_batch)
        #     print(example_batch_predictions.shape, "# (batch_size, sequence_length, vocab_size)")

        model.summary()

        # sampled_indices = tf.random.categorical(example_batch_predictions[0], num_samples=1)
        # sampled_indices = tf.squeeze(sampled_indices, axis=-1).numpy()
        #
        # print("Input: \n", repr("".join(idx2char[input_example_batch[0]])))
        # print()
        # print("Next Char Predictions: \n", repr("".join(idx2char[sampled_indices])))

        # example_batch_loss = loss(target_example_batch, example_batch_predictions)
        # print("Prediction shape: ", example_batch_predictions.shape, " # (batch_size, sequence_length, vocab_size)")
        # print("scalar_loss:      ", example_batch_loss.numpy().mean())

        checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
            filepath=checkpoint_prefix,
            save_weights_only=True)


        #model.load_weights(tf.train.latest_checkpoint(checkpoint_dir)) # Pickup Training from last checkpoint
        model.compile(optimizer='adam', loss=loss)

        EPOCHS = 1

        history = model.fit(dataset, epochs=EPOCHS, callbacks=[checkpoint_callback])
    elif args.generate:
        #tf.train.latest_checkpoint(checkpoint_dir)
        model = build_model(vocab_size, embedding_dim, rnn_units, batch_size=1)

        model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))
        #model.load_weights('checkpoints/ckpt_60')

        model.build(tf.TensorShape([1, None]))

        print(generate_text(model, str(args.seed)))
