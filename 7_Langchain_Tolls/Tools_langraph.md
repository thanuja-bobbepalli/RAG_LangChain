# Tools in LangChain

## Introduction

Tools are one of the most important components in LangChain, especially when building **Agents**.

A Tool allows a Large Language Model (LLM) to **interact with external systems or perform specific tasks**. While LLMs are excellent at generating text and reasoning, they cannot directly execute actions such as calling APIs, querying databases, or performing reliable calculations. Tools enable the model to perform these external operations.

In simple terms:

A **Tool = a function or capability that an agent can call to perform an action**.

By using tools, LLMs evolve from simple text generators into **action-capable intelligent systems**.

---

# Why Tools Are Needed

LLMs have several inherent limitations.

| Limitation | Example |
|---|---|
| No real-time knowledge | Current weather |
| Cannot access APIs | Stock prices |
| Cannot query private databases | Company records |
| Cannot execute programs | Running Python code |
| Weak reliability in calculations | Complex arithmetic |

Because of these limitations, LLMs alone cannot build many practical applications.

Tools solve this problem by enabling LLMs to **perform external operations and retrieve real information**.

Example scenario:

User asks:  
"What is the current temperature in Hyderabad?"

The LLM itself cannot know real-time weather. Instead, the **agent calls a weather tool**, which retrieves the data from a weather service and returns the result.

---

# Role of Tools in Agents

Tools are mainly used by **Agents**.

Agents are systems where the LLM is allowed to **reason about the task and decide what action to take**.

Workflow:

User Question  
↓  
Agent reasoning  
↓  
Select appropriate tool  
↓  
Tool execution  
↓  
Result returned to agent  
↓  
Final response generated

Example:

User asks:  
"What is the population of Japan?"

Agent reasoning:  
"This requires external information. I should use a knowledge retrieval tool."

Tool execution retrieves the population data.

Agent produces the final response using the tool output.

---

# Types of Tools in LangChain

LangChain tools can be broadly categorized into **two types**.

## 1. Built-in Tools

Built-in tools are **predefined tools provided by LangChain**.

These tools allow agents to interact with common external systems without requiring custom implementation.

Examples include:

- Web search tools
- Wikipedia query tools
- Python execution tools
- SQL database tools
- File system tools

These tools are already implemented and ready to use when building agents.

Advantages:

- Quick to use
- Minimal setup
- Tested integrations

Example usage scenario:

A research assistant agent may use a **Wikipedia tool** to retrieve information.

---

## 2. Custom Tools

Custom tools are **developer-defined tools** created for specific application requirements.

Developers create custom tools when built-in tools are not sufficient.

Examples include:

- Internal company API tool
- Custom database query tool
- Business logic functions
- Data analysis tools
- Machine learning inference tools

Custom tools allow agents to interact with **application-specific functionality**.

Example scenario:

A company chatbot might use a **customer database tool** to retrieve account information.

---

# Toolkits in LangChain

A **Toolkit** is a collection of related tools grouped together.

Instead of providing many individual tools to an agent, LangChain can provide a toolkit that contains multiple tools designed for a specific domain.

Example concept:

Toolkit  
├ Tool 1  
├ Tool 2  
├ Tool 3  

Example toolkit types:

Database toolkit might contain:

- Tool for listing database tables
- Tool for retrieving schema
- Tool for executing SQL queries

Advantages of toolkits:

- Organized tool management
- Easier integration with agents
- Reusable tool collections

---

# Ways to Create Tools in LangChain

LangChain provides **three main methods** to create tools.

These methods differ in complexity and flexibility.

---

# 1. Creating Tools Using the `@tool` Decorator

The simplest way to create a tool is by using the **tool decorator**.

In this approach, a normal Python function is converted into a LangChain tool.

The function includes:

- a clear description
- defined input parameters
- the logic of the operation

Example:

A function that multiplies two numbers.

Inputs: two integers  
Operation: multiply them  
Output: product of the numbers

This function is decorated with the tool decorator so that it becomes accessible to the agent.

Advantages:

- Very simple implementation
- Minimal code required
- Best for small utility functions

Typical use cases:

- simple calculations
- small API calls
- formatting functions

---

# 2. Structured Tools Using Pydantic

Structured tools allow defining **input schemas** using Pydantic models.

This ensures that the tool receives **well-structured and validated inputs**.

Instead of passing raw parameters, the tool defines a schema that describes the expected inputs.

Example scenario:

A multiplication tool may define a structured input model with:

Parameter A: integer  
Parameter B: integer  

The tool validates that the inputs match the schema before executing.

Advantages:

- Input validation
- Clear input structure
- Better compatibility with LLM reasoning

This method is useful when tools require **multiple parameters or structured input**.

Typical use cases:

- API requests
- database queries
- tools with many parameters

---

# 3. Creating Tools Using the Base Tool Class

The most advanced method for creating tools is by extending the **Base Tool class**.

In this approach, developers create a custom class that defines the behavior of the tool.

The class specifies:

- tool name
- tool description
- execution logic

Example scenario:

A custom multiplication tool class may define:

Tool name: multiply  
Description: multiplies two numbers  
Execution logic: returns the product of the inputs

Advantages:

- Maximum flexibility
- Full control over tool behavior
- Suitable for complex or production-level systems

Typical use cases:

- complex APIs
- multi-step operations
- enterprise applications

---

# Comparison of Tool Creation Methods

| Method | Complexity | Best Use Case |
|---|---|---|
| `@tool` decorator | Easy | Simple functions |
| Structured Tool with Pydantic | Medium | Tools with structured inputs |
| Base Tool class | Advanced | Complex custom tools |

---

# When Should Tools Be Used?

Tools should be used whenever the task requires **interaction with external systems or computations**.

Examples:

| Application | Tool Example |
|---|---|
Weather assistant | Weather API tool |
Financial assistant | Stock price API |
Database chatbot | SQL query tool |
Coding assistant | Python execution tool |
Search assistant | Web search tool |

---

# Interview Notes

### What is a Tool in LangChain?

A Tool is a function or capability that an agent can use to perform actions such as retrieving data, executing programs, or interacting with external services.

---

### Why Do Agents Need Tools?

Agents use tools to overcome the limitations of LLMs and perform real-world tasks.

---

### Difference Between Tools and Chains

| Tools | Chains |
|---|---|
Perform specific actions | Execute sequential workflows |
Used by agents | Used for pipeline execution |

---

# Key Takeaways from This Lecture

1. LLMs alone cannot interact with external systems.

2. Tools enable LLMs to perform actions such as API calls, database queries, and computations.

3. Agents decide **which tool to use** based on the user query.

4. LangChain provides both **built-in tools and custom tools**.

5. Developers can create tools in three ways:
   - tool decorator
   - structured tools with Pydantic
   - Base Tool class

6. Toolkits help organize multiple related tools into reusable collections.

7. Tools are fundamental for building **real-world agent-based AI systems**.

---

# Summary

Tools are a core building block in LangChain that enable LLM-powered agents to interact with external systems.

They allow agents to:

- access real-time information
- execute functions
- interact with APIs
- query databases
- perform computations

By integrating tools, LangChain transforms LLMs into **intelligent systems capable of performing real-world actions**.