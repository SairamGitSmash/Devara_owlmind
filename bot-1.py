##
## OwlMind - Platform for Education and Experimentation with Generative Intelligent Systems
## bot-1.py :: Getting Started with simple Discord Bot connected to a Rule-Based Bot engine
## 
#  
# Copyright (c) 2024 Dr. Fernando Koch, The Generative Intelligence Lab @ FAU
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# Documentation and Getting Started:
#    https://github.com/GenILab-FAU/owlmind
#
# Class Documentation at:
#    https://github.com/GenILab-FAU/owlmind/docs/bot-1.md
#
# Disclaimer: 
# Generative AI has been used extensively while developing this package.
# 

from dotenv import dotenv_values
from owlmind.discord import DiscordBot
from owlmind.simplebrain import SimpleBrain

from discord.ext import commands

if __name__ == '__main__':

    # load token from .env
    config = dotenv_values(".env")
    TOKEN = config['TOKEN']
    ## Alternative: Hard-code your TOKEN here and remote the comment:
    # TOKEN={My Token} 

    # Load Simples Bot Brain loading rules from a CSV
    brain = SimpleBrain(id='bot-1')
    brain.load('rules/new-rules.csv')

    # Kick start the Bot Runner process
    bot = DiscordBot(token=TOKEN, brain=brain, debug=True)

    faqs = {
    "What is the best way to study?": "The best way to study is through active recall, spaced repetition, and summarization.",
    "How can I improve focus?": "Try the Pomodoro technique, eliminate distractions, and take regular breaks."
}

bot = commands.Bot(command_prefix="/")

@bot.command()
async def faq(ctx, *, question: str):
    answer = faqs.get(question, "Sorry, I don't have an answer for that yet!")
    await ctx.send(answer)
    bot.run()

