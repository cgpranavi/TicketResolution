from google.adk.agents import Agent
from google.adk.tools import VertexAiSearchTool
YOUR_DATASTORE_ID = "projects/hacker2025-team-72-dev/locations/global/collections/default_collection/dataStores/ticketresolution_1750420895571"

vertex_search_tool = VertexAiSearchTool(data_store_id=YOUR_DATASTORE_ID)

# Agent Definition
root_agent = Agent(
    name= "docagent",
    model="gemini-2.0-flash", # Requires Gemini model
    tools=[vertex_search_tool],
     instruction=f"""You are a ticket support assistant. Use the search tool to find information about tickets in the datastore: {YOUR_DATASTORE_ID}.
                The datastore contains ticket information in a structured format (likely a CSV). You can search for tickets by ID or keywords.
                If you cannot find the information, respond with: "I couldn't find the information." """,
    # Example: "What is the status of ticket 12345?"
    description="Answers questions related to all the ID's from the csv file using the given datastore.",
)


# def get_ticket_data(ticket_id: str) -> dict:
#     """Retrieves ticket data from a hypothetical GCP data source.
#     Args:
#         ticket_id (str): The ID of the ticket to retrieve.
#     Returns:
#         dict: status and result or error message.
#     """
#     # In a real application, this would involve querying a GCP data source
#     # such as BigQuery or Cloud SQL.  Here, we simulate the behavior with
#     # hardcoded data for ticket ID "12345" and an error for other IDs.
#     if ticket_id == "12345":
#         return {
#             "status": "success",
#             "data": {
#                 "ticket_id": "12345",
#                 "title": "Unable to connect to VPN",
#                 "status": "Open",
#                 "priority": "High",
#                 "submitted_by": "user123",
#                 "submitted_at": "2024-01-20 14:30:00 UTC",
#             },
#         }
#     else:
#         return {"status": "error", "error_message": f"Ticket '{ticket_id}' not found."}
# root_agent = Agent(
#     name="ticket_resolution_agent",
#     model="gemini-2.0-flash",
#     description="Agent to answer questions about the ticket resolution process.",
#     instruction="I can answer your questions about the ticket resolution process.",
#     tools=[get_ticket_data]
# )
