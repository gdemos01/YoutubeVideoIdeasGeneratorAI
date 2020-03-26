# Youtube Video Idea Generator AI
<img width="100%" src="https://github.com/gdemos01/TwitterInfluencerAI/blob/master/data/KylieTrump.jpg">

This AI uses Natural Language Processing to generate new YouTube video titles / ideas? It was trained using 20000 video titles collected from some of the most popular YouTube channels.

### YouTube Video with Process and Results: PENDING

## How to use

### Collect YouTube Video Titles
Collect YouTube video titles using YouTube's Data API from a collection of channels defined in the code. You can add/remove YouTube channels through the code. In order for this to work you have to register for an API KEY.

```
python Controller.py --collect "YOUR API KEY"
```

### Train Model
The command bellow trains the model for 10 epochs. Each epoch creates a new checkpoint if the model is improved. You can change the input file and the number of epochs through the code.
```
python Controller.py --train
```

### Generate YouTube Titles
The command bellow generates a few YouTube titles based on a seed text that you provide. It builds the model based on the last training checkpoing.

```
python Controller.py --generate --seed="Hello world"
```

## Resources
* Twitter Influencer AI: https://github.com/gdemos01/TwitterInfluencerAI
* Text Generation with Python and TensorFlow/Keras (LSTM): https://stackabuse.com/text-generation-with-python-and-tensorflow-keras/
* Text Generation with Keras and TensorFlow video: https://www.youtube.com/watch?v=6ORnRAz3gnA
* Text Generation Using Tensorflow: https://www.tensorflow.org/tutorials/text/text_generation



