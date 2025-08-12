# LangChain & Ollama AI Exploration

This repository serves as an experimental playground to explore LangChain for building AI applications, leveraging Ollama as a local Large Language Model (LLM) backend.

## Overview

LangChain is a powerful framework designed to simplify the development of applications powered by language models. In this project, we integrate LangChain with Ollama, a locally hosted LLM, to experiment with AI workflows without relying on cloud-based models.

The goal is to understand how to:

	•	Connect LangChain with a local LLM instance via Ollama
	•	Build conversational agents and chain complex AI tasks
	•	Explore local inference with privacy and latency benefits

## Features
	1	Setup and connect LangChain with Ollama local LLM
	2	Basic conversational AI example using LangChain’s chains and prompts
	3	Experimentation with local LLM prompt engineering and response handling
	4	Extensible structure for adding advanced chains or integrations

## Getting Started

#### Pre-requisites
	•	Python 3.8+
	•	Ollama installed and running locally
	•	LangChain Python package
	•	Any additional dependencies listed in requirements.txt

#### Model Selection
I am using a Macbook Pro with 16 GB of RAM. So I prefer to use lighweight models under 6-7 GB.

My model selection strategy:

	•	llama3:8b for general tasks and prompting
    •	mistral:7b for tasks related to calling external tools

Run `ollama pull <model-name>` to download and use the model.