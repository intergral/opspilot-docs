# MCP: the Model Context Protocol

**MCP** - the [Model Context Protocol](https://modelcontextprotocol.io/introduction) - is a standardized way for software vendors to make their applications interface to AI tooling. Using MCP, AI models can get up-to-date information to augment their training models.

MCP was developed by [Anthropic](https://www.anthropic.com/news/model-context-protocol), but is vendor-neutral. Many AI providers offer MCP interfaces to their models, and many software vendors provide MCP interfaces into their products.

OpsPilot provides one MCP interface, the **OpsPilot MCP**.

## OpsPilot MCP

OpsPilot users can connect their AI tooling to their data using the [Model Context Protocol](https://modelcontextprotocol.io/introduction), a standard tool interface which allows AI models to communicate in real time with external tools.

MCP is used by many providers, including Claude Desktop, to help AI tooling access (and in some cases effect change in) external tools and systems.

The OpsPilot MCP is an integration of the [Grafana MCP](https://github.com/grafana/mcp-grafana) project.

!!! note
    The OpsPilot MCP is **read-only** for your telemetry data – you can’t change your account, dashboards, or data using it. The one exception is saving memories to the OpsPilot Coworker (see [Token usage](#token-usage)).

### Key capabilities

- Perform queries against Metrics (Mimir/Prometheus) and Logs (Loki).
- Get dashboards, panels, and the queries behind those panels – and run them directly (Prometheus and Loki only).
- Save information to the OpsPilot Coworker's memory using the `submit_memory` tool, so it can be used across the application.

### Token usage

When Claude is connected to OpsPilot through MCP, it interacts directly with your data using the tools exposed by the OpsPilot MCP. In most cases, this does **not** consume OpsPilot tokens.

- **Data queries:** Claude can access and query your data through the available MCP tools without incurring OpsPilot token charges. Claude handles the reasoning and processing of these requests, so the OpsPilot Coworker doesn't need to do the work.
- **Saving memories:** The main exception is the `submit_memory` tool. It saves information to the OpsPilot Coworker's memory so it can be accessed and used across the application. This operation consumes a small number of OpsPilot tokens.

In summary, connecting Claude through MCP lets you query and interact with your OpsPilot data without the standard OpsPilot AI token charges, except for specific operations such as saving memories.

!!! note
    Any token usage charged separately by your Claude provider remains subject to your agreement with that provider.


!!! info "Learn more"
    [Installing the OpsPilot MCP](/Monitor-your-data/MCP/MCP/)
