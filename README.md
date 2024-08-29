# Agi Metta

AGIMETTA is a project that integrates two AI techniques within a unified framework using the Hyperon framework. The project demonstrates how python functions are used with metta to perform specific tasks.

## The Agents

### News Agent

- **Purpose**: Fetched new articles from newsapi.
- **Functionality**: In AgiMetta, the news agent performs fetching a news article from newsapi.

### Sentiment Analysis Agent

- **Purpose**: Provides sentimental analysis based on the provided text description
- **Functionality**: This agent takes input and returns a if the sentiment is positive, negative or neutral.

### MeTTa Agent

- **Purpose**: Acts as the symbolic reasoner agent.
- **Functionality**: Calls the NEWS and SENTIMENT agents, stores and reads their outputs, and reasons over them using symbolic reasoning.

## Motivation

The AGIMETTA project aims to demonstrate how the Hyperon framework can be used as a unified environment to perform neural-symbolic reasoning. It shows how different python functions can be defined and utilized as grounded atoms within MeTTa, the programming language of the Hyperon framework.

## SetUp Guide

Clone the repo

```bash
git clone https://github.com/kecheste/agimetta.git
```

Cd to the repo

```bash
cd agimetta
```

Install the requirements

```bash
pip install -r requirements.txt
```

Run the metta file

```bash
metta run-agimetta.metta
```
