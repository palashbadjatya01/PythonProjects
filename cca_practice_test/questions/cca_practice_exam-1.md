# CCA Foundations — Practice Exam (60 Questions)


---

## Question 1
**Question:** You are building a 'Travel Assistant' that needs to check flight prices across 5 different APIs. Which approach offers the best user experience?

* A) Check each API one by one and show the user each result as it comes in.
* **B) Use a 'Streaming Join' pattern: stream the consolidated table to the user and update it in real-time as each API responds.**
* C) Only check the most popular API to keep latency low.
* D) Wait for all 5 APIs to return and show a single consolidated table.

**Correct Answer: B**
**Explanation:** Streaming Joins provide the best perceived performance. It gives the user immediate feedback while the heavier background tasks finish.

---

## Question 2
**Question:** When creating a 'Researcher Agent', you want it to look at a website and then write a report. You use the 'Fetch' MCP server. What is a key benefit of this server's design for your agent?

* A) It allows Claude to bypass paywalls and login screens automatically.
* B) It caches every website for 24 hours to save on API costs.
* C) It allows the agent to run JavaScript on the target page.
* **D) It automatically converts HTML to Markdown, which is more token-efficient and easier for Claude to read than raw HTML.**

**Correct Answer: D**
**Explanation:** Markdown preserves the structural semantic signal of a webpage (headings, links) while significantly reducing the noise and token count compared to raw HTML, improving model reasoning.

---

## Question 3
**Question:** A developer is building an MCP server to expose a custom internal API to Claude. They notice that Claude frequently confuses two tools, `query_db` and `search_logs`, because both accept a `query` string. What is the most efficient way to improve tool selection accuracy?

* A) Add `tool_use` examples for both tools in the global system prompt.
* B) Use `strict: true` in the tool definition to ensure the input schemas are strictly validated.
* C) Rename the tools to `Tool_A` and `Tool_B` to force Claude to rely on the system prompt for instructions.
* **D) Rewrite the tool descriptions to include 3-4 sentences detailing the specific data sources and explicit boundaries for each tool.**

**Correct Answer: D**
**Explanation:** Tool descriptions provide the semantic signal Claude uses to differentiate between capabilities. Detailed, boundary-focused descriptions are the most token-efficient way to ensure accuracy.

---

## Question 4
**Question:** Your agent is designed to 'cancel_subscription'. To prevent accidental churn, you want to guarantee the agent confirms the user's intent one last time before execution. Where should this logic be placed?

* A) By telling the model to "be very careful."
* **B) As a programmatic 'Pre-execution' gate that requires a specific boolean flag from a confirmation tool.**
* C) In the tool's description.
* D) In the system prompt's instructions.

**Correct Answer: B**
**Explanation:** High-stakes actions require programmatic gates. Relying on a prompt for confirmation is risky; a code-level requirement ensures compliance.

---

## Question 5
**Question:** A user wants to use Claude Code to perform a massive search-and-replace across 5,000 files. What is the most token-efficient way for Claude to handle this?

* A) Use the 'Agent Skills' feature to define a custom 'MultiFileReplace' skill.
* B) Upload all 5,000 files to the context window and ask for a single 'Refactor' response.
* **C) Instruct Claude to write a single Bash script to perform the replacement and run it using the 'Bash' tool.**
* D) Claude should open each file one by one, perform the edit, and save it.

**Correct Answer: C**
**Explanation:** One tool call (running a script) is significantly more efficient than 5,000 individual 'read-and-write' turns. Offloading repetitive bulk tasks to native environment tools is a core practice.

---

## Question 6
**Question:** You have built a multi-agent 'Research Team' where a 'Manager' agent delegates to 'Search' and 'Analyst' subagents. You find that the 'Manager' often gets confused and repeats the same search three times. How can you most efficiently improve the Manager's task tracking?

* **A) Implement a shared 'Scratchpad' or 'Status Board' tool that the Manager must update after every delegation.**
* B) Increase the penalty for repetitive tokens in the API settings.
* C) Instruct the subagents to include the phrase "TASK COMPLETE" in every response.
* D) Use a larger context window model like Claude 3 Opus.

**Correct Answer: A**
**Explanation:** Externalizing the state into a structured tool provides a persistent source of truth, preventing the model from losing its place in the conversation history.

---

## Question 7
**Question:** When creating a tool for an agent to `update_database_record`, why is it recommended to return the updated record as the tool result?

* **A) It allows the agent to verify that its requested changes were applied correctly without making an additional 'read' call.**
* B) It prevents 'tool selection ambiguity' in the next turn.
* C) It is required by the Model Context Protocol (MCP) specification.
* D) It ensures that the entire database is loaded into Claude's context for better reasoning.

**Correct Answer: A**
**Explanation:** High-fidelity tool design includes feedback loops. By seeing the result of its own action immediately, the agent can autonomously correct mistakes or confirm progress without wasting turns.

---

## Question 8
**Question:** You are building a multi-agent system where a 'Reviewer' agent needs to check the work of a 'Coder' agent. How should the system be architected to guarantee the Reviewer is unbiased?

* A) Have the Coder agent provide a summary of its logic to help the Reviewer understand the code.
* B) Instruct the Reviewer agent to be "critical but fair" in its system prompt.
* C) Run the Reviewer agent with a higher 'temperature' setting to encourage diverse perspectives.
* **D) Implement an 'Identity Blinding' pattern: the Reviewer should only see the output code, not the Coder's identity or previous reasoning steps.**

**Correct Answer: D**
**Explanation:** Agents can inherit the "hallucination paths" of previous agents. Identity Blinding ensures the Reviewer evaluates the artifact (the code) objectively, preventing confirmation bias.

---

## Question 9
**Question:** A engineer wants to use Claude Code to refactor a private repository that contains sensitive API keys. What is the recommended security practice?

* A) Only run Claude Code in 'read-only' mode.
* B) Ask Claude in the first turn to 'not look at sensitive files'.
* C) Encrypt the sensitive files so Claude can only see the filenames.
* **D) Add `.env` and other sensitive file patterns to a `.claudeignore` file.**

**Correct Answer: D**
**Explanation:** Security in Claude Code relies on explicit exclusion. The .claudeignore file is the primary way to ensure sensitive data is never indexed or included in the context window.

---

## Question 10
**Question:** You are extracting line items from thousands of physical receipts. Some receipts are blurry or have handwritten notes. Which architectural choice most enhances the reliability of this high-volume pipeline?

* **A) Implement a 'Multi-Pass' or 'OCR Pre-processing' step to compare results before finalizing.**
* B) Rely solely on a single system prompt to "try harder" with blurry text.
* C) Use only the highest temperature (1.0) to encourage creative deciphering of the text.
* D) Use the Batch API to process all receipts in a single large message to save cost.

**Correct Answer: A**
**Explanation:** Vision-based extraction from physical documents is probabilistic. High-reliability systems utilize consensus-based architectures or pre-processing steps to reduce hallucinations found in a single vision pass.

---

## Question 11
**Question:** A developer is using Claude Code to refactor a large legacy repository. They notice that Claude occasionally makes changes that violate the project's specific architectural patterns, such as placing business logic inside data access objects. Which configuration would most efficiently prevent these violations?

* A) Use plan mode for every interaction to manually review the architectural approach.
* B) Create a custom slash command for every refactoring task to include the rules.
* C) Update the global Claude Code system prompt via the CLI settings.
* **D) Add architectural guidelines to a CLAUDE.md file in the root directory.**

**Correct Answer: D**
**Explanation:** CLAUDE.md files are the primary mechanism for providing persistent, project-specific context and constraints, ensuring the model understands the ground rules before generation begins.


# CCAF Practice Exam Master Log: Questions 21–40

---

## Question 12
**Question:** A developer wants to guarantee that Claude Code's 'Auto-Fix' feature doesn't introduce any security vulnerabilities. What is the most comprehensive strategy?

* **A) Implement a 'Post-Process' hook that runs a Static Analysis Security Testing (SAST) tool on any file Claude modifies.**
* B) Instruct Claude to 'be very secure' in the `CLAUDE.md` file.
* C) Only allow Claude to work on 'non-sensitive' parts of the codebase.
* D) Use 'Claude 3.7 Opus' for all tasks.

**Correct Answer: A**
**Explanation:** Automated validation via a Post-Process hook ensures that every change is checked against security benchmarks programmatically before being finalized.

---

## Question 13
**Question:** You process 50,000 legal documents daily. You want 99.9% accuracy while keeping costs manageable. Which pattern is best?

* A) Use the Message Batches API with the 'temperature' set to 0.0.
* B) Process every document twice with Sonnet and compare.
* **C) Use Claude 3.5 Haiku for the initial extraction, then use a 'Verifier' agent (Sonnet) to check a random 5% sample and any 'low-confidence' flags.**
* D) Use Claude 3 Opus for every document.

**Correct Answer: C**
**Explanation:** The 'Triage and Verify' pattern is the most cost-effective for scale. Using a cheaper model for the bulk work and a premium model for verification maintains high reliability without extreme costs.

---

## Question 14
**Question:** An architect is designing an MCP server that needs to support both local developers using Claude Desktop and a cloud-based agentic system. Which transport method should they build?

* A) gRPC.
* B) STDIO only.
* **C) The server should support both STDIO for local use and HTTP+SSE for remote/cloud connections.**
* D) WebSockets.

**Correct Answer: C**
**Explanation:** MCP standardizes on STDIO for local integrations (child processes) and HTTP+SSE for remote cloud connections. Supporting both ensures full portability.

---

## Question 15
**Question:** You are building a research agent that uses an MCP server to access a database of scientific papers. The model often returns 'No results found' for specific queries because it fails to use the correct date format required by the database. Which solution offers the best developer experience and reliability?

* A) Provide 10 few-shot examples in the system prompt showing the exact date format required.
* B) Change the MCP server's database schema to accept any date format the model might produce.
* **C) Implement a 'Post ToolUse' hook to normalize the model's date output into the format required by the MCP server.**
* D) Instruct the model to first call a 'format_date' tool before calling the database tool.

**Correct Answer: C**
**Explanation:** Post ToolUse hooks are the most robust place to handle data normalization. Programmatic normalization ensures the tool call succeeds deterministically without needing the model to perfectly manage technical formats.

---

## Question 16
**Question:** Production data shows that in 12% of cases your agent skips `get_customer` entirely and calls `lookup_order` using only a name, leading to incorrect refunds. What change would most efficiently address this?

* A) Enhance the system prompt to state that verification is mandatory.
* B) Add few-shot examples showing the agent always calling `get_customer` first.
* **C) Add a programmatic prerequisite that blocks `lookup_order` until `get_customer` has returned a verified customer ID.**
* D) Implement a routing classifier that enables only specific tools.

**Correct Answer: C**
**Explanation:** Programmatic enforcement (hooks or gates) provides a deterministic guarantee. While prompts and few-shots improve performance, they are probabilistic. Making a verified ID a code-level prerequisite ensures the sequence is followed 100% of the time.

---

## Question 17
**Question:** An designer is choosing between 'Claude 3.7 Sonnet' and 'Claude 3.5 Haiku' for a tool-heavy agent. The agent must accurately choose between 50 different complex tools. Which factor most favors Sonnet?

* **A) Sonnet's higher reasoning capability makes it significantly better at 'Tool Selection' and 'Instruction Adherence' for large tool surfaces.**
* B) Sonnet is 50% cheaper when used with the Message Batches API.
* C) Haiku's faster latency is better for tool-calling loops.
* D) Sonnet supports 'tool_choice' while Haiku does not.

**Correct Answer: A**
**Explanation:** For an agent managing 50 tools, the reasoning load is high. Claude 3.7 Sonnet possesses superior architectural intelligence to correctly map intent to tool schemas without misrouting.

---

## Question 18
**Question:** In Claude Code, you want to specify a custom command `/review-security` that always uses a specific set of audit prompts. What should you create?

* A) A section in the `CLAUDE.md` file titled 'Slash Commands'.
* B) A custom 'Post ToolUse' hook.
* C) A bash alias in your `.zshrc` file.
* **D) A custom 'Agent Skill' in the `.claude/skills/` directory.**

**Correct Answer: D**
**Explanation:** Skills are the mechanism for extending the Claude Code CLI with new interactive commands. Defining a skill in the dedicated .claude/skills/ directory allows architects to standardize specialized, prompt-driven workflows.

---

## Question 19
**Question:** In an agentic workflow, a 'Coordinator' agent needs to wait for three different subagents to finish their independent research tasks. How should this be builded for maximum efficiency?

* **A) Implement a 'Join' or 'Await All' barrier to gather all context before moving to the synthesis step.**
* B) Instruct the subagents to call the Coordinator back individually as soon as they finish.
* C) Have the Coordinator poll each subagent sequentially every 5 seconds until all are complete.
* D) Set a fixed 60-second timeout and hope all agents finish within that window.

**Correct Answer: A**
**Explanation:** Managing parallel dependencies requires a barrier synchronization (Join/Await). This ensures that the next stage of the workflow—typically synthesis—has the complete set of data.

---

## Question 20
**Question:** An designer is designing a multi-agent system where a 'Coordinator' agent delegates tasks to a 'Research' agent and a 'Writing' agent. During testing, the 'Writing' agent fails to include the data found by the 'Research' agent, even though both are called by the same Coordinator. What is the fundamental cause of this failure?

* A) The Writing agent's system prompt was too long, causing it to ignore the context provided by the Coordinator.
* B) The Coordinator used a 'tool_choice' of 'auto' instead of 'any', leading to the delegation being skipped.
* **C) Subagents do not share a global memory; the Coordinator must explicitly include the Research agent's output in the prompt sent to the Writing agent.**
* D) The Research agent's output was not formatted as valid JSON, preventing the Writing agent from parsing it.

**Correct Answer: C**
**Explanation:** Subagents operate in isolated contexts. The Coordinator must act as the central relay, manually capturing the output from one agent and injecting it into the prompt of the next.

---

## Question 21
**Question:** A 'Summarizer' subagent includes irrelevant metadata from a 'Source_Reader' tool. Which architecture change best addresses this?

* A) Increase 'temperature' to 0.0.
* B) Instruct the 'Summarizer' to 'ignore metadata'.
* C) Use a 'Post ToolUse' hook to regex-out the metadata.
* **D) Modify 'Source_Reader' to return a 'High-Signal' cleaned version instead of raw output.**

**Correct Answer: D**
**Explanation:** Prioritize the Signal-to-Noise ratio at the source. Cleaning data at the tool level ensures downstream agents only receive useful information, preserving context and accuracy.

---

## Question 22
**Question:** An agent needs to choose between 100 different 'Customer Account' tools. You notice it frequently picks the wrong one. What is the most efficient way to improve its selection accuracy?

* **A) Group the 100 tools into 'Namespaces' (e.g., Billing, Technical, Privacy) and use a 'Router' agent to delegate to the correct group.**
* B) Use 'Claude 3 Haiku' because its faster speed allows it to 'try' more tools.
* C) Put all 100 tool descriptions into one massive System Prompt.
* D) Rename all the tools to include a number (e.g., 'tool_1', 'tool_2') to help the model track them.

**Correct Answer: A**
**Explanation:** Massive prompts lead to 'Recall Degradation'. Namespace partitioning reduces the 'Tool Surface Area' the model must consider at any one time, improving selection reliability.

---

## Question 23
**Question:** An architect is designing a multi-agent system for 'Legal Discovery'. They need to process 1,000,000 documents. Which combination of features is most suitable?

* A) Real-time Streaming API + 'Claude 3.7 Opus' for maximum accuracy.
* B) A single massive context window + 'Extended Thinking' mode.
* C) Claude Code for bulk editing + Prompt Caching for the documents.
* **D) Message Batches API for bulk processing + Subagent delegation for handling long documents.**

**Correct Answer: D**
**Explanation:** For massive, non-real-time throughput (1,000,000 documents), the Message Batches API provides the necessary scale and a 50% cost reduction. Additionally, Subagent delegation (Divide and Conquer) is required to process long documents that would otherwise exceed individual token limits or suffer from recall degradation.

---

## Question 24
**Question:** A engineer wants Claude to maintain a 'scratchpad' of findings across a long multi-file debugging session. What is the best way?

* A) Rely on automatic conversation history summarization.
* B) Enable the 'long_context' flag.
* **C) Create a 'SCRATCHPAD.md' file and instruct Claude to update it after every step.**
* D) Use 'plan' mode for every turn.

**Correct Answer: C**
**Explanation:** Externalizing the "mental model" into a persistent file (Scratchpad pattern) ensures critical findings remain at the top of focus, preventing them from being lost in cluttered conversation history.

---

## Question 25
**Question:** A researcher analyzes 20 different 50-page PDFs using Prompt Caching. They notice the first query is expensive, but subsequent ones are cheap. Why?

* A) The Batch API is being applied.
* B) The first query uses Opus, the rest use Haiku.
* **C) The first query triggers a 'Cache Write' (surcharge), while subsequent hits are 'Cache Reads' (90% discount).**
* D) Claude remembers the PDFs for free after the first upload.

**Correct Answer: C**
**Explanation:** Prompt Caching involves a "Write" cost (standard price + ~25% surcharge) to store the data, followed by massive "Read" discounts (~90% off) for subsequent hits using that identical context.

---

## Question 26
**Question:** An designer is designing a system to extract data from thousands of 100-page PDF legal contracts. What is the most cost-effective and reliable way to manage the context for this task?

* A) Convert the PDFs to images and use Claude 3.5 Sonnet's vision capabilities.
* B) Use a 'Sliding Window' approach where the PDF is broken into overlapping 5-page chunks.
* **C) Use 'Context Caching' for the common parts of the contracts and use Haiku for initial extraction of specific data points.**
* D) Load the entire 100-page PDF into the context window for every request.

**Correct Answer: C**
**Explanation:** Context Caching is the most powerful tool for cost-optimization when dealing with repetitive long-form content. By caching standard legal clauses, you only pay full price for the unique variables. Pairing this with Claude 3.5 Haiku provides high speed and low cost for high-volume extraction.

---

## Question 27
**Question:** You are deploying a 'Support Agent' that uses an MCP server to fetch customer history. How should you architecture the tool response for a 'get_user_history' call to minimize latency?

* **A) Return only the last 5 relevant events and high-signal identifiers like 'order_id' or 'case_status'.**
* B) Return the entire raw JSON dump from the database.
* C) Return the data in multiple small chunks using parallel tool calls.
* D) Return a summary of the history as a natural language string.

**Correct Answer: A**
**Explanation:** Returning filtered, high-signal data minimizes latency and preserves the model's focus by removing metadata noise.

---

## Question 28
**Question:** A pharma company extracts dosage info from 500-page PDFs. Claude often misses info in the middle sections. Which change most enhances extraction recall?

* A) Switch to Claude 3 Haiku for lower computational overhead.
* B) Increase 'max_tokens' to 128,000.
* **C) Implement a sliding window segmentation strategy with overlapping chunks processed by parallel subagents.**
* D) Use the Message Batches API.

**Correct Answer: C**
**Explanation:** The "Lost in the Middle" effect is a common LLM constraint. Segmentation ensures every part of the text is treated as a "beginning" or "end" for an agent, maximizing recall.

---

## Question 29
**Question:** A retail company wants to use Claude to process thousands of customer feedback emails every night to generate a sentiment report. Real-time response is not required. Which API feature offers the best balance of cost-efficiency and reliability?

* A) Streaming Messages API with Sonnet 3.5
* B) Standard Messages API with Prompt Caching
* **C) Message Batches API**
* D) Claude Code with a custom 'Sentiment' subagent

**Correct Answer: C**
**Explanation:** The Message Batches API offers a 50% cost reduction for tasks that can be completed within a 24-hour window, making it ideal for non-real-time bulk processing.

---

## Question 30
**Question:** You are building a 'Code Review' agent. You want it to be particularly strict about 'SQL Injection' vulnerabilities. Which prompt engineering technique is most efficient?

* A) Tell the model it is a 'Senior Security Engineer' and its job is at stake.
* B) Use 'Extended Thinking' mode and set the temperature to 1.0.
* **C) Define a 'Negative Constraint' with explicit 'Red-Line' examples of what constitutes a vulnerability.**
* D) Repeatedly use the word 'DANGER' in the system prompt.

**Correct Answer: C**
**Explanation:** Effective security agents require Adversarial Prompting techniques. Using Negative Constraints paired with concrete "Red-Line" examples provides the model with clear, actionable boundaries.

---

## Question 31
**Question:** A 'Researcher Agent' pulls data from a legacy API returning extensive, messy HTML tables. What is the best way to present this to Claude?

* A) Screenshot the table and send it as an image.
* **B) Implement an MCP server that fetches HTML and converts relevant rows into clean Markdown or JSON.**
* C) Pass the raw HTML directly.
* D) Use the 'Batch API' for each row.

**Correct Answer: B**
**Explanation:** This is the 'MCP as a Filter' pattern. Removing HTML "noise" preserves the context window, reduces cost, and improves the model's extraction accuracy by providing high-signal data.

---

## Question 32
**Question:** In a 'Multi-Pass' code review designerure, a 'Style Agent' and a 'Logic Agent' both review a Pull Request. Why is this better than one single agent doing both?

* A) The agents can 'argue' with each other to find the truth.
* B) It is 50% cheaper to run two agents than one large agent.
* **C) It prevents 'Attention Dilution' and allows each agent to use a specialized system prompt for higher precision.**
* D) It allows the use of the 'Message Batches API'.

**Correct Answer: C**
**Explanation:** Narrowing an agent's scope reduces the cognitive load on the model, preventing it from missing subtle logic bugs while it is distracted by surface-level syntax rules.

---

## Question 33
**Question:** A developer using Claude Code wants to guarantee Claude doesn't 'hallucinate' existing library functions. Which configuration file is best?

* A) package.json
* B) .gitignore
* C) README.md
* **D) CLAUDE.md**

**Correct Answer: D**
**Explanation:** CLAUDE.md is the primary location for project-specific technical context. It bridges the gap between Claude's general training data and the project's actual implementation patterns.

---

## Question 34
**Question:** When using 'Claude Code', what is the main purpose of the 'plan' mode?

* **A) To have Claude outline its intended actions and get human approval before any tools (like file writes) are actually executed.**
* B) To allow Claude to bypass the 200,000 token context limit.
* C) To enable Claude to use the 'Message Batches API' for long-running tasks.
* D) To allow Claude to write code faster by skipping the 'reasoning' phase.

**Correct Answer: A**
**Explanation:** Plan mode is a critical Human-in-the-Loop feature. It ensures that for "destructive" or large-scale changes, the AI "measures twice and cuts once" by presenting an architectural outline for review before executing any file-system or external tools.

---

## Question 35
**Question:** A support agent handles refunds. Policy states no refund over $500 can be processed without human approval. Which guarantees highest compliance?

* A) Add few-shot examples showing escalation.
* B) Add the limit to the system prompt.
* **C) Use a tool call interception hook (Pre ToolUse) to block any 'process_refund' where 'amount > 500'.**
* D) Create a separate 'high_value_refund' tool for humans only.

**Correct Answer: C**
**Explanation:** Deterministic business rules must be enforced programmatically. Interception hooks provide a 100% guarantee that the rule is followed at the code level.

---

## Question 36
**Question:** Your agent is failing to use the `search_database` tool correctly because it keeps passing a 'List' instead of the 'String' required by the API. What is the most durable fix?

* A) Use a 'Post ToolUse' hook to convert the list back into a string.
* **B) Update the Tool's Input Schema (JSON Schema) to explicitly define the parameter as 'type: string'.**
* C) Provide 10 few-shot examples showing a string being passed.
* D) Add a note in the system prompt: 'NEVER pass a list to the search tool.'

**Correct Answer: B**
**Explanation:** The JSON Schema is the source of truth for tool calls. Explicitly defining the type in the schema is a deterministic fix that guides the model's generation more effectively than prompts.

---

## Question 37
**Question:** You are building a multi-agent research system where a coordinator agent delegates to subagents for web search and document analysis. The synthesis subagent is failing to provide citations for its findings, even though the coordinator's system prompt explicitly requires them. What is the most probable cause?

* A) The synthesis subagent's 'allowedTools' list does not include the Citation tool.
* B) The coordinator is using the Task tool with incorrect parameters.
* **C) The coordinator forgot to pass the 'require citations' instruction to the synthesis subagent.**
* D) The web search subagent is not returning source URLs in its output.

**Correct Answer: C**
**Explanation:** Subagents operate with isolated context. They do not automatically inherit the parent's system prompts. To ensure specific behavior, requirements must be explicitly included in the prompt passed to the subagent.

---

## Question 38
**Question:** A researcher summarizes 50 academic papers using Prompt Caching. Which describes the cost implications?

* A) Caching reduces input and output costs by 50%.
* **B) Caching saves on input for repeated queries, but 'write' turns are more expensive than standard input.**
* C) Caching is automatic and doesn't change billing.
* D) Caching is only effective under 1,000 tokens.

**Correct Answer: B**
**Explanation:** Prompt Caching uses a "Write-Once, Read-Many" model. Initial storage has a surcharge, but subsequent "Read" hits are discounted by up to 90%. It has no effect on output token pricing.

---

## Question 39
**Question:** A financial services agent is authorized to 'get_account_balance' but must never 'transfer_funds' if the amount exceeds $10,000 without HITL approval. Which implementation offers a deterministic security guarantee?

* A) Add a 'Negative Constraint' in the system prompt.
* B) Use 'tool_choice' set to 'none' whenever a user mentions a large amount.
* C) Provide few-shot examples where the agent asks for permission for a $15,000 transfer.
* **D) Implement a 'Pre ToolUse' hook that intercepts 'transfer_funds' calls and triggers an approval workflow if the amount is > $10,000.**

**Correct Answer: D**
**Explanation:** For safety boundaries, programmatic enforcement (like hooks) is the only valid choice. Prompts are probabilistic and can be bypassed.


# CCAF Practice Exam Master Log: Questions 41–60

---

## Question 40
**Question:** A 'Content Moderation' agent needs to flag toxic comments. If it finds a comment it can't definitively classify, it should escalate to a human. Which designerural pattern is best for this?

* A) Use a 'Parallel Task' where a human and the AI both classify every comment.
* **B) Confidence-based routing where the agent is instructed to call an 'escalate_to_human' tool if its internal confidence score is below a threshold.**
* C) Instruct the agent to 'try its best' and only ask for help if it receives an error from the API.
* D) Set 'temperature' to 0.0 to ensure the model is always confident.

**Correct Answer: B**
**Explanation:** Defining clear escalation triggers (tools) is the industry-standard pattern for Human-in-the-Loop (HITL) systems, allowing autonomous processing for low-ambiguity cases.

---

## Question 41
**Question:** A 'Code Migrator' converts Java to Python. For a large project, the model often 'forgets' the Java class structure by the third file. What is the most probable cause?

* A) Python and Java have conflicting syntax.
* B) The Java code was provided in the system prompt.
* C) The developer is not using 'Extended Thinking' mode.
* **D) The model's attention is being diluted by the increasing amount of code in the context window.**

**Correct Answer: D**
**Explanation:** This is a classic case of Attention Dilution. As the history grows, the "signal" of the original class structure gets buried under the "noise" of newly generated code. Use a 'Master Reference' file to keep core architecture at the top of focus.

---

## Question 42
**Question:** When creating a multi-agent system using the Claude Agent SDK, you want to spawn three subagents to analyze three different documents simultaneously. How should the coordinator agent initiate this?

* A) Ask the user to upload the documents one by one to avoid rate limits.
* B) Send all three documents to a single subagent with a high context window to save costs.
* C) Call each subagent sequentially in a `for` loop to ensure context is shared.
* **D) Use the `parallel` execution pattern provided by the Claude Agent SDK to trigger all three subagents at once.**

**Correct Answer: D**
**Explanation:** For independent tasks, the Claude Agent SDK is designed to support Parallel Execution, which minimizes total wall-clock time (latency) by processing sub-tasks concurrently.

---

## Question 43
**Question:** An agentic system for 'Automated Security Auditing' needs to run for several hours, exploring a codebase and running various scanners. How can you avoid the session from becoming too 'heavy' and slow?

* A) Use 'Claude 3 Haiku' for all reasoning to save tokens.
* **B) Implement a 'Document & Clear' pattern: periodically save findings to a markdown file, run `/clear`, and start a fresh session reading that file.**
* C) Disable 'Prompt Caching' to ensure each turn is fresh.
* D) Increase the 'max_tokens' to 200,000 for every turn.

**Correct Answer: B**
**Explanation:** Long-context performance degradation is a physical constraint. The 'Document & Clear' pattern acts as a manual context reset, preserving findings in a file while flushing the history to maintain high-signal reasoning.

---

## Question 44
**Question:** A engineer wants to share a specific 'Code Review' workflow with their entire team in Claude Code. Where should they save it?

* A) In a global CLAUDE.md in /etc.
* **B) In a .claude/agents/ or .claude/skills/ directory at the project root and check it into Git.**
* C) As a custom alias in .bashrc.
* D) In local ~/.claude/.

**Correct Answer: B**
**Explanation:** This is "Agent Config as Code." Placing settings in the project root's .claude directory and checking it into version control ensures every developer on the project has consistent tools.

---

## Question 45
**Question:** A developer is using Claude Code and sees the message: 'Claude is requesting permission to run `rm -rf /`'. How can the project architect avoid this from ever happening again?

* **A) Add a 'Pre ToolUse' hook that regex-checks all 'Bash' commands and blocks anything containing 'rm -rf'.**
* B) Tell the developer to review every command.
* C) Add 'Do not use rm -rf' to the project's CLAUDE.md file.
* D) Set the `permissionMode` to 'strict' in global settings.

**Correct Answer: A**
**Explanation:** This follows the 'Hook as a Firewall' pattern. Only a Pre ToolUse hook provides a programmatic, deterministic "fail-safe" that works regardless of the model's reasoning or the user's attentiveness.

---

## Question 46
**Question:** A retail company wants to use Claude to process 50,000 product reviews to extract 'Pros' and 'Cons' in JSON format for a weekly report. Which approach is most cost-effective?

* A) Deploy a fleet of 100 parallel Haiku subagents.
* B) Use Claude Code's bulk refactor mode.
* **C) Use the Message Batches API.**
* D) Implement Prompt Caching for the product catalog.

**Correct Answer: C**
**Explanation:** The Message Batches API is the standard architectural choice for high-volume, asynchronous workloads. It provides a 50% discount compared to standard API calls, making it the most cost-effective choice for a weekly 50k review process.

---

## Question 47
**Question:** A developer is using Claude Code to refactor a Python project. They want to guarantee Claude uses 'pytest' instead of 'unittest'. They add this rule to `CLAUDE.md`, but Claude still occasionally tries to run `python -m unittest`. What is the likely reason?

* A) `CLAUDE.md` only supports instructions for Node.js projects, not Python.
* B) The developer forgot to put 'IMPORTANT' in all caps next to the instruction.
* **C) The project still contains 'unittest' files that Claude is discovering and using as examples of established patterns.**
* D) The developer has reached the 200,000 token context limit.

**Correct Answer: C**
**Explanation:** Claude is an in-context learner. It often prioritizes "the truth of the code" (existing patterns) over instructions in CLAUDE.md. If the repository is full of unittest examples, the model assumes those are the standard it should follow.

---

## Question 48
**Question:** You are extracting data from legal contracts and need the output to follow a specific JSON schema with nested arrays. Which feature guarantees adherence?

* A) A very detailed system prompt with 5 examples.
* **B) Structured Output (Beta) with a defined JSON Schema.**
* C) Using the 'Message Batches API' with a validation script.
* D) Setting the model's 'stop_sequences' to '}'.

**Correct Answer: B**
**Explanation:** Structured Output uses constrained decoding to ensure the model's response is mathematically guaranteed to match the provided JSON schema, unlike probabilistic prompting.

---

## Question 49
**Question:** Structured extraction receives a 'stop_reason' of 'max_tokens' and truncated JSON. What is the best immediate fix?

* A) Switch to 'tool_choice' type 'any'.
* **B) Increase the 'max_tokens' value.**
* C) Enable 'extended thinking'.
* D) Implement a retry loop to 'fix' the JSON.

**Correct Answer: B**
**Explanation:** A `max_tokens` stop reason is a deterministic signal that the model was physically cut off. Increasing the token budget allows the model to complete the full output string.

---

## Question 50
**Question:** During a complex multi-agent research task, you notice the coordinator agent frequently re-assigns the same sub-topic to different subagents, leading to redundant work and high token usage. What is the most probable architectural flaw?

* A) The 'Task' tool does not support parallel execution, causing the coordinator to lose track.
* **B) The coordinator is performing overly narrow task decomposition without tracking progress.**
* C) The system prompt for the subagents is too long, causing them to forget their assignments.
* D) The subagents are not sharing a global memory space to see each other's work.

**Correct Answer: B**
**Explanation:** The coordinator is responsible for task decomposition and delegation. Redundant assignments indicate a failure in partitioning the research scope or a lack of tracking which sub-topics have already been addressed.

---

## Question 51
**Question:** A 150-turn Claude Code session is causing the model to hallucinate log contents. What is the best recovery step?

* A) Enable 'Extended Thinking' mode.
* **B) Use /clear to reset context and provide a fresh summary of current findings.**
* C) Switch to Claude 3 Opus.
* D) Add a 'Priority' flag to CLAUDE.md.

**Correct Answer: B**
**Explanation:** This addresses Context Bloat. Wiping the noisy history with `/clear` and re-introducing high-signal facts restores reasoning fidelity that large models or thinking modes cannot recover in a saturated window.

---

## Question 52
**Question:** An MCP server needs a 'SessionID' header that expires every 30 minutes. How should the MCP server handle this?

* A) The MCP server should return an error and ask the model to call `refresh_token`.
* B) Use a 'Post ToolUse' hook to inject the header.
* C) The model should provide a valid 'SessionID' in tool arguments.
* **D) The MCP server should manage the session lifecycle internally, refreshing the token as needed.**

**Correct Answer: D**
**Explanation:** The 'Separation of Concerns' principle dictates that technical infrastructure (auth, session management) should be invisible to the agent. Handling it inside the MCP server prevents wasting tokens on infrastructure management.

---

## Question 53
**Question:** A structured data extraction pipeline is processing thousands of medical invoices. Some invoices cause the model to occasionally produce malformed JSON. Which strategy offers the best balance of reliability and efficiency?

* A) Switch to a smaller, faster model.
* **B) Implement a validation-retry loop that catches JSON errors and sends the error message back to the model for correction.**
* C) Increase the `max_tokens` parameter.
* D) Manually review every invoice.

**Correct Answer: B**
**Explanation:** A validation-retry loop allows the system to autonomously correct structural errors by feeding the error back to the model, which is highly scalable for production.

---

## Question 54
**Question:** A developer is building a 'Code Review' agent using the Claude Agent SDK. The agent is tasked with reviewing a pull request containing 15 files. To optimize for both cost and speed, the architect decides to use a 'Coordinator' agent that spawns subagents. Which orchestration pattern best fulfills these requirements while staying within the 200k token limit?

* A) Spawn 15 subagents sequentially, one for each file.
* **B) Use the `parallel` execution pattern to analyze all 15 files concurrently, then have the Coordinator synthesize the results.**
* C) Send all 15 files to a single subagent in one massive prompt.
* D) Use the Message Batches API to review each file individually over 24 hours.

**Correct Answer: B**
**Explanation:** Parallel execution via the SDK optimizes for speed while allowing each file to be processed with fresh context, preventing the 200k limit from becoming a bottleneck.

---

## Question 55
**Question:** A support agent has two tools: `search_faq` (fast) and `deep_search_docs` (slow). How should you instruct Claude to select?

* A) Set 'tool_choice' to 'auto' with no guidance.
* **B) In the tool descriptions, specify that 'search_faq' is the first choice and 'deep_search_docs' is a fallback.**
* C) Remove 'search_faq' entirely.
* D) Put the instructions in the system prompt only.

**Correct Answer: B**
**Explanation:** Tool descriptions are the primary mechanism for routing. Placing usage instructions directly in the tool metadata ensures the model evaluates constraints at the exact moment of selection.

---

## Question 56
**Question:** An architect wants to guarantee that Claude Code follows the team's 'Prettier' and 'ESLint' configurations. What is the most robust way to achieve this?

* A) Create a custom 'Agent Skill' that includes the linting rules.
* B) Rely on the CI/CD pipeline to catch errors after Claude pushes the code.
* **C) Implement a 'Pre ToolUse' hook that runs linting/formatting on any modified files and rejects the turn if they fail.**
* D) Add a 'Coding Standards' section to the root CLAUDE.md file.

**Correct Answer: C**
**Explanation:** Programmatic hooks provide a deterministic guarantee. While CLAUDE.md provides guidance, a Pre ToolUse hook acts as a local gate that prevents non-compliant code from ever being finalized.

---

## Question 57
**Question:** You are building a data extraction tool for medical records. You need to guarantee the 'PatientID' is always a 10-digit number. Which feature should you use to guarantee this format?

* A) The Message Batches API.
* B) A 'Post ToolUse' hook that validates the ID and asks the model to retry.
* C) A detailed prompt explaining the 'PatientID' format with 10 examples.
* **D) Structured Output with a JSON Schema.**

**Correct Answer: D**
**Explanation:** Structured Outputs use constrained decoding to ensure the model's response mathematically matches the schema, providing certainty rather than probability.

---

## Question 58
**Question:** You are configuring Claude Code for a large monorepo. You want to guarantee that Claude follows specific React testing patterns in the `/frontend` directory but uses different Go benchmarks in the `/backend` directory. What is the most efficient configuration strategy?

* **A) Place a general `CLAUDE.md` in the root, and directory-specific `CLAUDE.md` files in both `/frontend` and `/backend`.**
* B) Use the 'Agent Skills' frontmatter in every source file to define the testing rules.
* C) Create custom slash commands for `/test-frontend` and `/test-backend` that contain the rules.
* D) Include all instructions for both React and Go in a single `CLAUDE.md` at the repository root.

**Correct Answer: A**
**Explanation:** Claude Code supports progressive disclosure via a directory hierarchy. Subdirectory CLAUDE.md files only activate when working in those folders, preventing "context leakage" between different tech stacks.

---

## Question 59
**Question:** A developer wants to guarantee Claude Code never modifies the `.env.production` file. Which is most robust?

* A) Set file permissions to read-only.
* **B) Create a 'Pre ToolUse' hook script that blocks attempted writes to that file.**
* C) Rename the file.
* D) Add 'DO NOT TOUCH' to CLAUDE.md.

**Correct Answer: B**
**Explanation:** Hooks provide 100% enforcement. Exiting with a specific code triggers a rejection the model cannot bypass, whereas prompts are probabilistic and permissions provide less useful context to the model.

---

## Question 60
**Question:** You are extracting names and dates from a collection of scanned historical letters. Many letters have overlapping dates and similar names, leading to confusion in the model's output. Which prompt engineering technique would most enhance accuracy?

* A) Repeat the instructions three times in the system prompt for emphasis.
* B) Tell the model: 'You are an expert historian. Do not make mistakes.'
* C) Use the 'Extended Thinking' parameter to give the model more time to process each letter.
* **D) Provide 3-5 'Chain of Thought' few-shot examples that show the model step-by-step how to disambiguate a complex letter.**

**Correct Answer: D**
**Explanation:** Few-shot examples are the highest-leverage tool. Providing Chain of Thought examples shows the model the specific logical steps to differentiate between similar entities.

---
