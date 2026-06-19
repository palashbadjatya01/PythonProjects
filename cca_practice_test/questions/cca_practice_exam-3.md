# CCA Foundations — Practice Exam 3 (60 Questions)

---

## Question 1
**Question:** What is the primary benefit of the Message Batches API for an enterprise processing 1 million documents a month?

* A) Support for images and multimodal inputs.
* **B) 50% lower cost per token compared to the real-time Messages API.**
* C) Higher reasoning quality for complex tasks.
* D) Real-time streaming of results as they are processed.

**Answer: B**
**Explanation:** The Batch API is designed for high-volume non-interactive workloads where immediate response is not required. Its primary value is significant cost optimization offering a 50% discount. It is asynchronous returning results within 24 hours and does not provide higher reasoning quality or real-time streaming.


---

## Question 2
**Question:** Which MCP SDK method is used to define a new tool that can be called by the Claude client?

* A) server.register()
* **B) server.tool()**
* C) client.createTool()
* D) mcp.addTool()

**Answer: B**
**Explanation:** The server.tool method is the standard way to register a tool its input schema and its execution logic in the MCP SDK. Tools are defined and hosted on the Server. The Client is responsible for discovering and calling them.


---

## Question 3
**Question:** Which JSON structure is required for an MCP tool definition to specify that a parameter named count must be an integer between 1 and 10?

* A) count: { val: 1-10, format: int }
* **B) count: { type: integer, minimum: 1, maximum: 10 }**
* C) count: int(1,10)
* D) params: [ { name: count, range: [1, 10] } ]

**Answer: B**
**Explanation:** The Model Context Protocol relies on standard JSON Schema for tool input validation. This ensures that the agent provides correctly formatted and bounded data before the tool is even executed. Using type minimum and maximum is the official way to enforce these constraints.


---

## Question 4
**Question:** A engineer wants to use Prompt Caching for a RAG system. The system uses a 50k token Company Handbook and a 5k token User History. What is the most efficient caching strategy?

* A) Create a separate cache breakpoint for every 100 tokens in the prompt.
* B) Apply a cache control block only to the User History section.
* **C) Place the 50k token handbook at the beginning of the prompt with a cache control block followed by the user history.**
* D) Place the dynamic User History first then the Company Handbook.

**Answer: C**
**Explanation:** Caching works from the top down. Placing the largest most static content first maximizes the number of tokens saved and ensures the cache is not invalidated by smaller frequently changing sections.


---

## Question 5
**Question:** A engineer is using Claude Code and wants to automatically run npm install every time they open the session. How can this be done?

* A) Add npm install to a .clauderc file in the home directory.
* **B) Claude Code does not support On-Startup scripts. It is designed for interactive task-driven workflows.**
* C) Put the instruction Run npm install first in the CLAUDE.md file.
* D) Add a Pre-Session hook in the .claude/hooks directory.

**Answer: B**
**Explanation:** Claude Code is a task-centric tool where proactive actions are driven by the agent reasoning about a specific goal rather than shell-like startup configurations. While it supports command hooks it does not currently have a global startup execution trigger.


---

## Question 6
**Question:** An MCP server tool for SQL Query is being abused by the agent to delete tables. How should the architect fix this?

* A) Use Extended Thinking to help the agent realize that deleting tables is bad.
* B) Add DROP TABLE to the .claudeignore file.
* **C) The MCP server should use a database user with Read-Only permissions.**
* D) Tell the agent Only perform SELECT queries in the system prompt.

**Answer: C**
**Explanation:** Secure tool design requires the Principle of Least Privilege in the underlying implementation. Security should be enforced at the infrastructure level rather than relying on soft prompt instructions which can be bypassed.


---

## Question 7
**Question:** A engineer is using few-shot prompting to help Claude extract SKU numbers. The model keeps getting the Format wrong. What is the best architectural fix?

* A) Use tool_choice to force the extraction into a regex-validated field.
* B) Tell the model Think step-by-step about the SKU format.
* C) Switch to a smaller model to save cost.
* **D) Provide 5 diverse few-shot examples that specifically show different SKU formats.**

**Answer: D**
**Explanation:** Few-shot prompting is the most powerful prompt engineering tool for anchoring model behavior to specific patterns. Diversity in few-shot examples helps the model generalize better to real-world data variations and is the primary way to improve internal extraction logic.


---

## Question 8
**Question:** Which part of the Claude Agent SDK is responsible for handling the Turn-Based loop between the model and the tools?

* A) The MCP Server.
* **B) The Orchestrator or Agent class.**
* C) The Cache Controller.
* D) The System Prompt.

**Answer: B**
**Explanation:** The Claude Agent SDK simplifies agent development by managing the complex User-Assistant state transitions. While the server provides the tools the SDK Client specifically the Orchestrator or Agent class is what manages the execution loop automatically handling tool calls and sending results back to the model until a final answer is reached.


---

## Question 9
**Question:** In an agentic system the Orchestrator needs to process 100 independent subtasks. What is the best way to handle this without hitting rate limits?

* A) Build Prompt Caching for each subtask.
* B) Use a single agent and process the tasks one by one in a loop.
* **C) Use the Message Batches API to submit all 100 tasks at once.**
* D) Launch 100 parallel subagents using the real-time Messages API.

**Answer: C**
**Explanation:** The Message Batches API is specifically designed for high-throughput non-latency-sensitive workloads. It offers higher rate limits and a 50% discount compared to real-time API calls making it the ideal choice for bulk processing where immediate responses are not required. Sequential loops are too slow and 100 parallel real-time calls are likely to trigger rate limit errors.


---

## Question 10
**Question:** In an agentic Code Migration task the agent gets stuck in a loop trying to fix the same syntax error. What should the Coordinator do?

* **A) Escalate to a human and provide the agent Thinking logs to help the human understand the struggle.**
* B) Clear the agent memory and restart the task from scratch.
* C) Raise the temperature to 1.0 to find a creative fix.
* D) Force the agent to use a smaller model for the next 10 turns.

**Answer: A**
**Explanation:** Human-in-the-loop escalation is a primary reliability pattern. Providing the Thinking logs allows the human to see exactly where the agent logic failed facilitating a faster resolution to the deadlock.


---

## Question 11
**Question:** Which of the following content blocks correctly formats a tool result for the Messages API?

* A) { tool_id: id-123, result: Success }
* B) { role: tool, content: Success }
* **C) { type: tool_result, tool_use_id: id-123, content: Success }**
* D) { type: tool_output, id: id-123, data: Success }

**Answer: C**
**Explanation:** A tool_result block must include the specific type field the tool_use_id that matches the original request from the model and the content of the result. These blocks are strictly required to be placed inside a message with the user role when sent back to the API.


---

## Question 12
**Question:** An MCP server tool keeps timing out after 10 seconds. Where should the engineer look to increase the timeout limit?

* A) In the .claudeignore file.
* B) In the MCP server TypeScript code.
* **C) In the Client configuration such as Claude Desktop or custom SDK settings.**
* D) In the system prompt for the model.

**Answer: C**
**Explanation:** Timeouts are typically enforced by the Client the caller to prevent the agent from hanging indefinitely. While a server can have internal timeouts the hard limit that terminates the connection is controlled by the client initiating the request.


---

## Question 13
**Question:** An agentic system uses a Planner agent to create a list of steps and an Executor agent to run them. The Executor keeps failing on step 3. What should the architect change?

* **A) The Planner should produce a Plan-to-File CLAUDE.md that the Executor can read and update as it progresses.**
* B) The Executor should be given a higher Extended Thinking budget.
* C) The Planner should be replaced with a hardcoded Python script.
* D) The Coordinator should force the Executor to restart from step 1 every time it fails.

**Answer: A**
**Explanation:** In complex multi-step tasks using a shared state file like CLAUDE.md provides external memory for the agents. This allows the Executor to track progress understand context from previous steps and resume effectively if a specific step fails rather than losing state or requiring a full restart.


---

## Question 14
**Question:** You are using the thinking parameter in Claude Sonnet. How are the reasoning tokens billed?

* **A) Reasoning tokens are billed as Output Tokens at the standard rate.**
* B) Reasoning tokens are billed as Input Tokens.
* C) Reasoning tokens are billed at a 90% discount like cache hits.
* D) Reasoning tokens are free of charge.

**Answer: A**
**Explanation:** Extended Thinking tokens are billed as standard Output Tokens. Architects must account for these when setting max_tokens limits and calculating turn costs as they represent the model internal computational work.


---

## Question 15
**Question:** A engineer wants to change the default editor used by Claude Code for editing files. Which configuration method is correct?

* A) Add Use Vim for all edits to the CLAUDE.md file.
* **B) Claude Code uses its own internal agentic tools for file editing. It does not rely on an external EDITOR environment variable.**
* C) Update the config.json file with editor_path: /usr/bin/vim.
* D) Set the EDITOR environment variable to code or vim.

**Answer: B**
**Explanation:** Claude Code is a headless agent that performs edits directly via its own tool-calling logic rather than spawning an external process like a traditional CLI.


---

## Question 16
**Question:** A engineer is implementing a Plan-to-File pattern where an agent writes its multi-step strategy to a file. Which file name is the standard convention for this in a Claude Code environment?

* A) PLAN.txt
* B) agent-state.log
* **C) CLAUDE.md**
* D) instructions.json

**Answer: C**
**Explanation:** CLAUDE.md is the recognized source of truth for project context and agentic planning within the Claude Code ecosystem. It serves as the external memory for the agent providing a stable reference point across sessions.


---

## Question 17
**Question:** A engineer needs to extract a list of Action Items from a meeting transcript. The output must be a JSON array of strings. Which prompt is best?

* **A) Extract action items and return them as a JSON array of strings: [ item1, item2 ]**
* B) Make a list of what people need to do.
* C) Use the ActionExtractor tool to get the items.
* D) Return the action items in JSON format.

**Answer: A**
**Explanation:** Providing specific constraints and a few-shot formatting example is the most reliable way to get correctly formatted JSON. Vague prompts lead to bulleted text while asking for JSON format without a schema can lead to inconsistent field names.


---

## Question 18
**Question:** A engineer needs Claude to generate a valid Terraform file. Which technique best prevents the use of deprecated resource names?

* **A) Provide a Reference Doc containing only the current valid resource names and use it as a RAG context.**
* B) Use the Message Batches API.
* C) Tell the model Do not use deprecated features.
* D) Set the temperature to 0.0.

**Answer: A**
**Explanation:** Grounding the model with up-to-date documentation is the most reliable way to prevent the use of outdated knowledge. Factual technical accuracy is a context problem and RAG is the standard solution for providing current data that exceeds the model training cutoff.


---

## Question 19
**Question:** In a Plan-to-File pattern why should the agent check off completed steps in the CLAUDE.md file?

* A) To provide a persistent state that allows the agent to resume correctly if the session is interrupted or context is lost.
* B) To notify the human user via a Slack integration hook.
* C) To trigger a cache-hit for the remaining tokens in the file.
* **D) To provide the agent with a visual sense of progress and prevent it from repeating finished tasks.**

**Answer: D**
**Explanation:** Updating the state in a file acts as working memory ensuring the agent stays on track during multi-turn tasks and does not repeat work. It also provides a persistent state that allows for session resumption.


---

## Question 20
**Question:** A engineer is using Claude Code and wants to ignore all .tmp files and any directory named build. What should the .claudeignore file look like?

* A) [EXCLUDE] tmp_files=.tmp build_dir=build/
* **B) .tmp /build/**
* C) IGNORE .tmp AND build/
* D) --exclude .tmp --exclude build/

**Answer: B**
**Explanation:** The .claudeignore file follows standard glob patterns similar to .gitignore to exclude files and directories from the agent context. Proper context pruning improves security and prevents the agent from wasting tokens on junk files or build artifacts.


---

## Question 21
**Question:** Which architectural component is responsible for Token Counting and Budget Management in the Claude Agent SDK?

* **A) The Monitor class.**
* B) The User Message.
* C) The System Prompt.
* D) The MCP Server.

**Answer: A**
**Explanation:** In the Claude Agent SDK Monitors track resource usage including tokens turns and costs and can enforce policies when budgets are exceeded.


---

## Question 22
**Question:** In an MCP architecture what is a Prompt from the server perspective?

* A) An action that the agent takes on the server filesystem.
* **B) A reusable text template that the client can use to start a conversation or perform a specific task.**
* C) A database query executed by the agent.
* D) A real-time notification sent from the server to the client.

**Answer: B**
**Explanation:** MCP Prompts allow servers to offer pre-configured instructions or shortcuts to the client. They provide discovery for common tasks helping users understand how to interact with the server. Unlike Tools which are for actions Prompts are informational and instructional templates.


---

## Question 23
**Question:** In the Contextual Retrieval pattern what is the role of the Subagent?

* A) To convert the document from PDF to Text.
* **B) To read individual document chunks and write a 1-2 sentence context-setting prefix for each.**
* C) To act as the main search engine for the user.
* D) To encrypt the document chunks for security.

**Answer: B**
**Explanation:** Contextual Retrieval ensures that small chunks of text do not lose their meaning when separated from the source document. A subagent analyzes each chunk relative to the whole file and prepends a brief summary significantly improving retrieval accuracy in RAG systems.


---

## Question 24
**Question:** An agent is analyzing a large codebase. What is the benefit of using Contextual Retrieval over standard Top-K vector search?

* A) It automatically fixes any bugs found in the retrieved code.
* **B) It prepends a brief summary of the whole file to each chunk ensuring the model understands the chunk purpose.**
* C) It allows the model to read the entire codebase in a single turn.
* D) It uses Prompt Caching to make the search 90% cheaper.

**Answer: B**
**Explanation:** Contextual Retrieval is an Anthropic technique designed to solve the decontextualization problem in RAG. By prepending a brief document-wide context to each individual chunk before embedding the system ensures that small snippets retain their meaning even when pulled in isolation during a vector search.


---

## Question 25
**Question:** Which stop_reason value is returned by the Messages API when the model needs to call a tool to proceed?

* A) max_tokens
* **B) tool_use**
* C) stop_sequence
* D) end_turn

**Answer: B**
**Explanation:** The tool_use stop reason indicates that the model has generated one or more tool calls and is awaiting the results. Architects must check this reason to determine if they need to execute the tool on the backend and send the results back to the model to continue the conversation.


---

## Question 26
**Question:** A engineer is using tool_choice to force a FinalAnswer tool. The model is still outputting Here is your answer before the tool call. How to fix?

* **A) Add a negative constraint to the system prompt: Output ONLY the tool call. Do not include any conversational filler.**
* B) Use the Message Batches API.
* C) Set the temperature to 0.0.
* D) Raise the thinking budget.

**Answer: A**
**Explanation:** Achieving perfect structured-only output often requires a combination of API parameters and explicit prompt constraints. While tool_choice forces the inclusion of a tool call the model may still include conversational preamble unless specifically instructed to omit it via the system prompt.


---

## Question 27
**Question:** A lead architect is designing a system where a Coordinator agent must delegate a complex coding task to a subagent. Which architectural pattern ensures the Coordinator can verify the subagent work without re-executing the entire task?

* A) Prompt Caching: Cache the subagent output to speed up subsequent turns.
* **B) Reviewer-Correction Pattern: Use a separate Reviewer agent to evaluate the subagent output against a predefined rubric.**
* C) Single-Agent Loop: Have the same subagent check its own work 5 times.
* D) Zero-Shot Delegation: Trust the subagent first output and merge it immediately.

**Answer: B**
**Explanation:** Using a dedicated Reviewer agent provides an independent evaluation allowing the Coordinator to verify quality based on the reviewer feedback.


---

## Question 28
**Question:** An agentic Data Analyst keeps crashing because it retrieves a 500000-row dataset into its context. What is the best fix?

* A) Use Prompt Caching for the 500000 rows.
* B) Raise the max_tokens parameter in the API request.
* C) Switch to a larger model for its infinite context capability.
* **D) Build a Summarize or Aggregate step in the database tool to return high-signal statistics instead of raw data.**

**Answer: D**
**Explanation:** Proper agentic architecture requires data reduction. Instead of dumping raw data into the context window tools should be designed to aggregate or summarize data at the source providing the agent with only the relevant insights needed for reasoning.


---

## Question 29
**Question:** When using forced tool use with the tool_choice parameter what is a primary limitation the architect must consider?

* A) The model is forbidden from using any other tools in that specific turn.
* **B) The model will likely skip providing a conversational thought or explanation before the tool call.**
* C) The model temperature is automatically locked to 0.0.
* D) The request will always be billed at a higher Priority rate.

**Answer: B**
**Explanation:** Forcing a tool causes the model to jump directly to the tool call output. This headless mode eliminates the conversational preamble and visible reasoning that typically precedes a response in a standard turn.


---

## Question 30
**Question:** Which API parameter should be used to ensure that Claude follows a complex logic path without skipping steps?

* A) system: Think step-by-step
* B) top_k: 1
* **C) thinking: { type: enabled, budget_tokens: 2000 }**
* D) stop_sequences: [ step ]

**Answer: C**
**Explanation:** Extended Thinking allows the model to use internal reasoning tokens to work through logic before providing a final response. While Chain-of-Thought prompting is useful, the thinking parameter provides a more robust reasoning capacity.


---

## Question 31
**Question:** What is the function of the CLAUDE.md file in a Claude Code project?

* **A) To provide the agent with project-specific instructions, coding standards, and architectural context.**
* B) To list the dependencies and libraries used in the project.
* C) To store the user Anthropic API key and billing details.
* D) To act as a changelog for the project git commits.

**Answer: A**
**Explanation:** CLAUDE.md acts as a specialized system prompt extension for the local project environment. It is the most important file for customizing Claude Code, providing how to develop guidance rather than just project metadata or sensitive credentials.


---

## Question 32
**Question:** A engineer is using Claude Sonnet for a coding task. They notice the model is making logical leaps and missing edge cases. Which API parameter should be enabled?

* **A) thinking: { type: enabled, budget_tokens: 4000 }**
* B) max_tokens: 100000
* C) temperature: 1.0
* D) top_p: 0.1

**Answer: A**
**Explanation:** Extended Thinking allows the model to use an internal reasoning scratchpad. This system 2 reasoning helps the model work through complex logic and edge cases that standard generation might overlook.


---

## Question 33
**Question:** Which command is used to initialize a new MCP project using the official TypeScript template?

* A) mcp init --template typescript
* B) npm install mcp-server-ts
* **C) npx @modelcontextprotocol/create-server**
* D) claude mcp create

**Answer: C**
**Explanation:** The create-server tool is the official utility to bootstrap a new MCP server with the correct directory structure and dependencies.


---

## Question 34
**Question:** In a long conversation you want to cache the System Prompt and the Initial Project Requirements. How many cache breakpoints do you need?

* A) Unlimited
* B) 1
* C) 4
* **D) 2**

**Answer: D**
**Explanation:** Anthropic Prompt Caching is prefix-based. To optimize a session with two distinct static blocks you place one breakpoint at the end of the System Prompt and a second at the end of the Requirements. The API supports up to 4 breakpoints.


---

## Question 35
**Question:** A engineer wants to use Claude Code to build a project from scratch. Which command should they use to ensure the agent understands the full requirements?

* A) claude --init
* **B) claude Build a project based on the requirements in requirements.txt**
* C) claude generate-code
* D) claude --task build-all

**Answer: B**
**Explanation:** Referencing a specific file containing the requirements is the best way to give the agent a complete north star for the task. Agentic project inception works best when the agent has a clear written set of requirements to reference.


---

## Question 36
**Question:** A high-security financial agent is being designed. Which stop_reason should trigger an immediate human review before any further action is taken?

* A) The agent returns end_turn.
* **B) The agent attempts to call a tool named execute_wire_transfer.**
* C) The agent uses Extended Thinking.
* D) The agent hits max_tokens.

**Answer: B**
**Explanation:** High-stakes tools should be gated by Human-in-the-Loop workflows to prevent unauthorized or erroneous transactions. Reliability in sensitive domains is achieved by gating state-changing tools with human approval.


---

## Question 37
**Question:** Which MCP concept allows a server to notify a client that a specific piece of data such as a file has changed?

* A) Tool-Callbacks
* B) Polling
* **C) Subscriptions and Notifications**
* D) Heartbeats

**Answer: C**
**Explanation:** Subscriptions allow clients to stay in sync with changing data. The server sends a Notification whenever a resource is updated.


---

## Question 38
**Question:** A engineer is using the Claude Agent SDK and wants to define a custom Policy that limits an agent to only 5 tool calls per task. Where is this built?

* A) In the .claudeignore file.
* **B) In the Agent configuration or a custom Monitor class within the SDK.**
* C) In the MCP server configuration.
* D) In the system prompt: Do not use more than 5 tools.

**Answer: B**
**Explanation:** The Claude Agent SDK allows for granular control over agent behavior through policies and monitoring hooks. Hard execution limits to prevent infinite loops or runaway costs are most reliably enforced within the SDK orchestration layer using monitors or configuration policies.


---

## Question 39
**Question:** In an Agentic Search workflow how should the Coordinator handle a subagent that keeps hallucinating non-existent research papers?

* A) Use the Message Batches API for the research tasks.
* B) Tell the subagent to be more honest in the system prompt.
* **C) Add a Verifier tool that performs a real-time web search for the paper DOI or title to confirm its existence.**
* D) Switch the subagent temperature to 1.0.

**Answer: C**
**Explanation:** Grounding agent claims in real-world verification tools is the standard way to eliminate hallucinations in technical tasks. Providing functional verification tools that give a source of truth is significantly more effective than moralizing instructions or increasing temperature.


---

## Question 40
**Question:** In a long multi-turn session the cost of each turn is increasing rapidly. What is the most effective way to reduce costs?

* **A) Build Prompt Caching with a breakpoint after every 5-10 turns.**
* B) Switch to a smaller model for every 3rd turn.
* C) Reduce the max_tokens parameter to 500.
* D) Clear the conversation history every 5 turns.

**Answer: A**
**Explanation:** Prompt Caching is the most effective feature for cost-optimizing long-running agentic conversations. Caching the conversation history ensures you only pay for new turns at full price while old turns are billed at a significantly lower rate.


---

## Question 41
**Question:** A engineer wants Claude Code to refactor a project. They notice Claude keeps trying to use a library that is not installed. How can this be corrected?

* A) Raise the temperature to 1.0 to encourage creativity.
* **B) Update CLAUDE.md with a list of Allowed Libraries and Forbidden Libraries.**
* C) Use a .claudeignore file to hide the package.json file.
* D) Delete the library documentation from the local node_modules folder.

**Answer: B**
**Explanation:** CLAUDE.md is the most effective place to set boundaries and project-specific technical constraints. It acts as the operational playbook for the agent preventing it from deviating from project standards or hallucinating dependencies based on its training data.


---

## Question 42
**Question:** In an agentic research pipeline the Search Agent keeps returning 404 errors for every URL it tries. What is the best Self-Healing mechanism to build?

* A) Hardcode the agent to only use one specific verified URL.
* B) The tool should automatically retry the same URL 10 times.
* **C) The tool should return the 404 error text and the agent system prompt should include instructions on how to use a different search engine.**
* D) The Coordinator should stop the Search Agent and start a new one.

**Answer: C**
**Explanation:** Semantic error handling allows the agent to reason about the failure. By returning the 404 error and providing fallback logic in the prompt the agent can autonomously decide to pivot its strategy or try a different source.


---

## Question 43
**Question:** Which CLI command in Claude Code allows you to switch between models for the current session?

* A) claude switch haiku
* B) claude --model haiku
* C) claude set-engine haiku
* **D) claude config**

**Answer: D**
**Explanation:** The claude config command or the interactive menu it opens is the standard way to manage persistent session settings including model selection. While flags like --model can be used at startup config is used to switch or manage preferences within the environment.


---

## Question 44
**Question:** Which MCP transport is recommended for high-performance local communication between a client and a server on the same machine?

* A) HTTP with JSON-RPC.
* B) WebSockets.
* C) gRPC over local loopback.
* **D) Standard Input/Output stdio.**

**Answer: D**
**Explanation:** Stdio is the default and most efficient MCP transport for local integrations as it eliminates network overhead and simplifies security.


---

## Question 45
**Question:** Which MCP protocol message is used by the client to discover what tools a server offers?

* **A) tools/list**
* B) server/get-tools
* C) tools/discover
* D) mcp/init-tools

**Answer: A**
**Explanation:** The MCP protocol uses a specific namespace/method structure. The tools/list request is the standard way for an MCP client to retrieve the definitions and schemas of all available tools from a server. This discovery process typically happens after the initial handshake.


---

## Question 46
**Question:** Which JSON Schema property is used in a tool definition to ensure the model provides a value for a specific argument?

* A) default: must-provide
* B) optional: false
* **C) required: [ argument-name ]**
* D) is-mandatory: true

**Answer: C**
**Explanation:** The required array at the top level of the properties object specifies which fields the model must populate. Defining required fields is essential for preventing tool calls with missing data that cause backend failures.


---

## Question 47
**Question:** What does a cache_hit signify in the billing details of an Anthropic API call?

* A) The tool execution result was successfully retrieved from a cache.
* **B) The tokens were retrieved from the server-side cache and billed at a 90% discount.**
* C) The model response was already stored in a local database.
* D) The user previous message was identical to the current one.

**Answer: B**
**Explanation:** Prompt Caching significantly reduces the cost of repeated or large static prompt segments. A cache_hit means the prefix of your prompt matched a previously cached segment on Anthropic servers allowing those tokens to be processed at a much lower price point and with lower latency.


---

## Question 48
**Question:** A engineer wants to ensure that Claude Code never commits code that has not been linted. What is the best implementation?

* **A) A PreToolUse hook that runs the linter and exits with code 2 if it finds errors.**
* B) A git pre-commit hook in the local .git directory.
* C) A line in CLAUDE.md saying Always lint your code before committing.
* D) Setting the model temperature to 0.0.

**Answer: A**
**Explanation:** Hard safety and quality constraints should be moved out of the prompt and into the hook system. Hooks provide a programmatic guarantee that a condition is met before an action like a commit is allowed and they provide better feedback directly into the agent conversation loop.


---

## Question 49
**Question:** You are configuring Claude Code for a large monorepo. Claude is hitting the context limit because it keeps reading too many files. How do you fix this?

* A) Instruct Claude in CLAUDE.md to only look at 5 files at a time.
* B) Raise the Prompt Caching TTL.
* **C) Use .claudeignore to hide irrelevant directories and sub-projects from the agent view.**
* D) Switch to a larger model for its larger context window.

**Answer: C**
**Explanation:** Pruning the available file tree using .claudeignore ensures the agent only indexes relevant source files saving context tokens.


---

## Question 50
**Question:** Which agentic pattern is most suitable for a Customer Support agent that needs to verify user identity before accessing account data?

* A) Single-Agent Zero-Shot: Trust the agent to ask for a password before calling the get-account tool.
* B) Message Batches API: Submit all support requests in a single batch once a day.
* **C) Gatekeeper Pattern: A dedicated agent handles authentication and only hands off the session to the Support agent once verified.**
* D) Parallel Execution: Run the Identity Check and the Account Access in parallel to save time.

**Answer: C**
**Explanation:** In high-security architectures separating authentication from general task assistance is critical. The Gatekeeper Pattern ensures that sensitive tools are only available after a specialized authentication agent has verified the user.


---

## Question 51
**Question:** A engineer is building an MCP server in Python. Which library is the official way to implement the Model Context Protocol?

* A) anthropic-mcp-lib
* B) langchain-mcp-adapter
* C) mcp-core-python
* **D) mcp-python-sdk**

**Answer: D**
**Explanation:** The official mcp-python-sdk provides the standardized classes and decorators for creating MCP servers and clients ensuring compatibility across the ecosystem.


---

## Question 52
**Question:** You are creating an MCP tool that returns a list of files. How should the tool indicate a Generic Error such as Folder not found to Claude?

* A) Throw an unhandled exception in the MCP server TypeScript code.
* B) Return an empty string.
* **C) Set is_error: true in the tool result and provide the error message in the content.**
* D) Return a JSON object: { status: fail, code: 404 }.

**Answer: C**
**Explanation:** The is_error flag is the official MCP method for signaling failure allowing the model to reason about the error instead of treating error text as valid data.


---

## Question 53
**Question:** An MCP server is being used to provide access to a legacy database. The database is slow taking 30 seconds to return results. How should the tool be designed?

* **A) The tool should accept an email parameter and send the results asynchronously once the query is complete.**
* B) The tool should return Loading and the agent should use a loop to check the status every second.
* C) The tool should be split into 10 smaller tools that each take 3 seconds.
* D) The tool should block the agent until the 30 seconds are up.

**Answer: A**
**Explanation:** Asynchronous results prevent timeouts and allow the agent to continue assisting the user while the heavy lifting happens in the background.


---

## Question 54
**Question:** A engineer is implementing a complex workflow where an agent must first Plan a series of shell commands and then Execute them. Which approach best minimizes the risk of the agent executing a destructive command by mistake?

* **A) Build a PreToolUse hook that parses the command and requires manual shell confirmation for any rm or chmod operations.**
* B) Use the Message Batches API to run the commands in a sandbox environment.
* C) Add a Safety Officer subagent that reads the agent logs every 30 minutes.
* D) Raise the Extended Thinking budget to 10000 tokens to ensure the agent thinks more about safety.

**Answer: A**
**Explanation:** Safety in agentic systems should be layered combining prompt instructions with deterministic execution hooks. Hooks provide a programmatic safety gate that intercepts tool calls before they are executed allowing for manual or automated validation. While reasoning helps it is probabilistic. A hard-coded hook provides a deterministic safety guarantee.


---

## Question 55
**Question:** **Question 1**

* A) if [[ $COMMAND == 'rm -rf' ]]; then return 1; fi
* B) case $1 in 'rm -rf') exit 0;; esac
* **C) if [[ $CLAUDE_COMMAND == 'rm -rf' ]]; then exit 2; fi**
* D) echo 'Blocked' && stop-agent

**Answer: C**
**Explanation:** Claude Code hooks use standard shell logic but rely on exit code 2 to signal a rejection which blocks the tool execution. Exit code 0 allows the command while exit code 1 is a generic script error. The environment variable CLAUDE_COMMAND is used to evaluate the specific command being run.


---

## Question 56
**Question:** An architect wants to cache a 150k token Technical Specification that is used by 20 different agents. What is the most important consideration?

* A) All 20 agents must use the same model.
* B) The specification must be updated every 5 minutes to keep the cache fresh.
* C) The specification must be placed at the very end of the prompt.
* **D) The specification must be identical character-for-character in every request for the cache hit to occur.**

**Answer: D**
**Explanation:** Prompt Caching relies on exact prefix matching. Even a single extra space or a slight change in the system prompt before the cached block will invalidate the cache hit.


---

## Question 57
**Question:** An agentic system for Travel Planning uses a subagent to find hotels. Sometimes the subagent returns hotels that are sold out. What is the best architectural fix?

* A) Raise the Extended Thinking budget to 8000 tokens.
* **B) Give the subagent a Check Availability tool and update its instructions to use it before reporting results.**
* C) Instruct the Coordinator to double check the subagent work.
* D) Switch the subagent to a larger model.

**Answer: B**
**Explanation:** In agentic workflows hallucinations or outdated information are often solved by providing better tools rather than just more reasoning power. By giving the subagent a tool to verify real-time data you close the loop between the model training data and the current state of the world.


---

## Question 58
**Question:** A engineer is building a Code Review agent. Which architectural pattern minimizes the risk of the agent missing critical security flaws?

* A) Parallel Subagents: 10 agents look at 10 different files simultaneously.
* B) Standard RAG: Retrieve similar bugs from the past and show them to the agent.
* **C) Multi-Pass Review: Agent A identifies potential flaws and Agent B a Senior persona verifies and filters them.**
* D) Single-Agent CoT: Use one agent with a very long Extended Thinking budget.

**Answer: C**
**Explanation:** Layering agents with different prompts creates a safety model for better accuracy. High-reliability systems use verification loops where independent agents check each other work which is more effective at catching blind spots than simply increasing thinking time or using parallel speed.


---

## Question 59
**Question:** When extracting structured data why is it better to use tool_use than just asking for raw JSON in the text?

* **A) The tool_use mechanism provides built-in schema validation and a more deterministic output format.**
* B) Tool use is 50% cheaper than standard text output.
* C) Tool use allows the model to think for longer.
* D) Tool use automatically caches the result.

**Answer: A**
**Explanation:** Using tools forces the model to adhere to a formal JSON structure making it much easier for downstream code to parse. While text-based JSON requests can be prone to conversational filler or formatting errors tool_use ensures the output matches a predefined schema.


---

## Question 60
**Question:** A engineer wants Claude to write a Post-Mortem report based on 10 log files. The model keeps getting confused by the timestamps. What is the best fix?

* A) Use Extended Thinking with a 10000 token budget.
* B) Tell the model to be an expert in log analysis.
* **C) Pre-process the logs to convert all timestamps to a relative format before sending them to Claude.**
* D) Use the Message Batches API to process each log file separately.

**Answer: C**
**Explanation:** Cleaning and normalizing data before it hits the model is a key architect skill. Structural data improvement is the most effective way to ensure accuracy when dealing with complex temporal relationships compared to just increasing reasoning time.


---
