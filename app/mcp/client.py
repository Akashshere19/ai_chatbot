from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp import ClientSession


class MCPToolClient:

    async def call_tool(self, tool_name: str, arguments: dict):

        server = StdioServerParameters(
            command="python",
            args=["-m", "app.mcp.server"],
        )

        async with stdio_client(server) as (read_stream, write_stream):

            async with ClientSession(
                read_stream,
                write_stream
            ) as session:

                await session.initialize()

                result = await session.call_tool(
                    tool_name,
                    arguments=arguments
                )

                return result.content

        # self.transport =  await stdio_client(server)

        # self.session = ClientSession(self.transport)

        # await self.session.initialize()

    # async def call_tool(self, name: str, arguments: dict):

    #     result = await self.session.call_tool(
    #         name=name,
    #         arguments=arguments
    #     )

    #     return result.content