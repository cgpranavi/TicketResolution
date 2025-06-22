from google.adk.agents import Agent


def get_ticket_data(ticket_id: str) -> dict:
    """Retrieves ticket data from a hypothetical GCP data source.
    Args:
        ticket_id (str): The ID of the ticket to retrieve.
    Returns:
        dict: status and result or error message.
    """
    # In a real application, this would involve querying a GCP data source
    # such as BigQuery or Cloud SQL.  Here, we simulate the behavior with
    # hardcoded data for ticket ID "12345" and an error for other IDs.
    if ticket_id == "12345":
        return {
            "status": "success",
            "data": {
                "ticket_id": "12345",
                "title": "Unable to connect to VPN",
                "status": "Open",
                "priority": "High",
                "submitted_by": "user123",
                "submitted_at": "2024-01-20 14:30:00 UTC",
            },
        }
    else:
        return {"status": "error", "error_message": f"Ticket '{ticket_id}' not found."}

root_agent = Agent(
    name="ticket_resolution_agent",
    model="gemini-2.0-flash",
    description="Agent to answer questions about the time and weather in a city.",
    instruction="I can answer your questions about the time and weather in a city.",
    tools=[get_ticket_data]
)