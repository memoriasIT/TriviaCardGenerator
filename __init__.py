#!/usr/bin/env python3.6
# coding=utf-8

# Get data from OpenTriviaDatabase
import requests
import json
import html
import random

# Database
from tinydb import TinyDB, Query
import os

# Make image
from PIL import Image, ImageDraw, ImageFont
import textwrap

# Generate logs
import logging
import sys


#  __________________________________________
# [          - QUESTION OBJECT -             ]
#
class Question:
    def __init__(self):
        data = html.unescape(self.getData())

        self.responseCode = data['response_code']
        self.category = html.unescape(data['results'][0]['category'])
        self.correctAnswer = html.unescape(data['results'][0]['correct_answer'])
        self.incorrectAnswer = html.unescape(data['results'][0]['incorrect_answers'])
        self.qst = html.unescape(data['results'][0]['question'])
        self.type = html.unescape(data['results'][0]['type'])

    def getData(self):
        try:
            # OpenTriviaDatabase API
            url = "https://opentdb.com/api.php?amount=1"

            # Call API and get data
            data = requests.get(url)
            logging.getLogger("ImageGenerator")
            logging.info("Data retrieved successfully")
            return data.json()

        except requests.exceptions.Timeout:
            # Retry
            logging.warning("Connection timed-out, retrying...")
            self.getData()
        except requests.exceptions.TooManyRedirects:
            # URL incorrect
            logging.error("Too many redirects detected, bad URL perhaps?")
            sys.exit(1)
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            logging.error(e)
            sys.exit(1)

    def generateAnswers(self):
        # Add all answers in the list (including the correct answer)
        answerlist = [self.correctAnswer]
        for answer in self.incorrectAnswer:
            answerlist.append(answer)

        # Make the correct answer be in a random place in the list (shuffle)
        return (random.sample(answerlist, len(answerlist)), self.correctAnswer)

#  __________________________________________
# [          - GENERATE IMAGE -             ]
#
# Generates image with python PIL
def generateImage(qst, strSave):
    # Set Logger to print info too (change if wanted)
    logging.basicConfig(level = logging.INFO)
    log = logging.getLogger("ImageGenerator")
    #path = os.path.dirname(__file__)
    path = os.getcwd()

    # Use JSON file as database for better search times
    try:
        categoryDict = TinyDB(path+'/categoryDict.json')
    except Exception as e:
        log.error("Critical error while handling database")
        print(e)
        sys.exit(1)

    try:
        # Select the background according to category
        query = Query()
        dbResult = categoryDict.search(query.category == qst.category)[0]
        img = Image.open(os.path.join(path,dbResult['background']))

        # Get height and witdh of image to generate graphics according to it
        imgw, imgh = img.size

        # Initialize font with different sizes
        font = ImageFont.truetype(os.path.join(path, 'assets/font.ttf'), 32)
        fontAnswer = ImageFont.truetype(os.path.join(path, 'assets/font.ttf'), 30)
        fontTitle = ImageFont.truetype(os.path.join(path, 'assets/font.ttf'), 48)
        draw = ImageDraw.Draw(img)

        # Starting Y coordinates
        y_text = round(imgh * 0.1)

        # Print category image
        til = Image.open(os.path.join(path, dbResult['icon'])).convert('RGBA')
        img.paste(til, (50, y_text), til)
        y_text += til.size[1] + 10

        # Print Title
        title = "QUESTION:"
        draw.text((50, y_text), title, font=fontTitle, fill=(255, 255, 255))
        y_text += fontTitle.getsize(title)[1] + 20

        # Print Question
        lines = textwrap.wrap(str(qst.qst), width=35)
        for line in lines:
            height = font.getsize(line)[1]
            draw.text(((imgw - 580), y_text), line, font=font, fill=(255, 255, 255))
            y_text += height

        # Print answers
        answers = qst.generateAnswers() # format: (["answers"], "correct answer")
        y_text += 20

        idx = 65
        correctAnswerYCoord = -1
        for answer in answers[0]:
            # Save y coordinate and letter of correct answer to generate image with correct answer later
            if (answer == qst.correctAnswer):
                correctAnswerYCoord = y_text
                correctAnswerIdx = idx

            # Answers might be multiline
            lines = textwrap.wrap(chr(idx) + ". " + answer, width=35)
            for line in lines:
                draw.text((50, y_text), html.unescape(line), font=fontAnswer, fill=(255, 255, 255))
                y_text += font.getsize(line)[1]+10

            idx += 1

        # Save Image without answers
        img.save(os.path.join(path, "output/"+strSave+"_0.png"))
        log.info("Image WITHOUT answers was saved successfully")

        # Draw correct answer in the same position (overwritten in green)
        # Answers might be multiline
        lines = textwrap.wrap(chr(correctAnswerIdx) + ". " + qst.correctAnswer, width=35)
        y_text = correctAnswerYCoord
        for line in lines:
            draw.text((50, y_text), html.unescape(line), font=fontAnswer, fill=(51, 153, 51))
            y_text += font.getsize(line)[1]+10

        # Save image with answer
        img.save(os.path.join(path, "output/"+strSave+"_1.png"))
        log.info("Image WITH answers was saved successfully")

    except IOError as e:
        log.error(e)
        sys.exit(1)
    except KeyError as e:
        log.error(e)
        sys.exit(1)


#  __________________________________________
# [          -       MAIN      -             ]
#
# strSave    -> Name to save the output file 
# e.g. test  -> test_0.png; test_1.png
def genImageMain(strSave):
    # Generate a question image into output folder
    q1 = Question()

    # Generate image
    generateImage(q1, strSave)




