import argparse
from NLP import NLP
from YoutubeAPI import  YoutubeAPI


if __name__ == '__main__':

    print("\n WELCOME TO YOUTUBE VIDEO IDEA GENERATOR AI \n\n")
    print(  "╭━┳━╭━╭━╮╮\n",
            "┃┈┈┈┣▅╋▅┫┃\n",
            "┃┈┃┈╰━╰━━━━━━╮\n",
            "╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣\n",
            "╲┃┈┈┈┈┈┈┈┈┈▉▉▉\n",
            "╲┃┈┈┈┈┈┈┈┈┈◥▉◤\n",
            "╲┃┈┈┈┈╭━┳━━━━╯\n",
            "╲┣━━━━━━┫﻿\n\n")

    parser = argparse.ArgumentParser()
    parser.add_argument("--train", action="store_true")
    parser.add_argument("--generate",action="store_true")
    parser.add_argument("--seed")
    parser.add_argument("--collect")
    args = parser.parse_args()

    if args.collect:
        print("> Collecting YouTube Video Titles from...well....YouTube")
        youtube_api = YoutubeAPI(str(args.collect))
        youtube_api.createDataset()
    else:
        text = open('titles.txt', 'rb').read().decode(encoding='utf-8')
        nlp = NLP()
        dataset, vocabulary = nlp.preprocess(text)
        dataset, vocabulary_size, embedding_dimension, rnn_nodes, batch_size = nlp.prepareSettings(dataset,vocabulary)

        if args.train:
            model = nlp.build_model(vocabulary_size,embedding_dimension,rnn_nodes,batch_size)
            nlp.trainModel(dataset,model,"./checkpoints",10)
            model.summary()
        elif args.generate:
            print(nlp.generate_text(vocabulary_size, embedding_dimension, rnn_nodes,"./checkpoints",str(args.seed)))
        else:
            print("\n> What are you doing dummy? Use the menu options")
