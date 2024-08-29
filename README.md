# AGIMETTA

AGIMETTA is a project that integrates two AI techniques within a unified framework using the Hyperon framework. The project demonstrates how Python functions are used with MeTTa to perform specific tasks.

## The Agents

### News Agent

- **Purpose**: Fetches news articles from NewsAPI.
- **Functionality**: In AGIMETTA, the News Agent fetches a news article based on a query parameter from NewsAPI and processes the description for further use.

### Sentiment Analysis Agent

- **Purpose**: Provides sentiment analysis based on the provided text description.
- **Functionality**: This agent analyzes the sentiment of the input text and returns whether the sentiment is positive, negative, or neutral.

### MeTTa Agent

- **Purpose**: Acts as the symbolic reasoner agent.
- **Functionality**: Calls the News and Sentiment agents, stores and reads their outputs, and performs symbolic reasoning based on the results.

## Motivation

The AGIMETTA project aims to demonstrate how the Hyperon framework can be used as a unified environment to perform neural-symbolic reasoning. It shows how different Python functions can be defined and utilized as grounded atoms within MeTTa, the programming language of the Hyperon framework.

## Setup Guide

1. **Clone the repository:**

   ```bash
   git clone https://github.com/kecheste/agimetta.git
   ```

2. **Navigate to the repository:**

   ```bash
   cd agimetta
   ```

3. **Install the requirements:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the MeTTa file:**

   ```bash
   metta run-agimetta.metta
   ```

## Example Usage

To use the News and Sentiment agents in MeTTa, you can run the following commands in the MeTTa file:

```metta
!(import! &self agimetta)
!(news "Tesla")
!(sentiment "Tesla is revolutionizing the electric vehicle market with innovative technology.")
! (add-reduct &self (news "Tesla"))
!(match &self $x $x)
```
