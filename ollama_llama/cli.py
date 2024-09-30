import argparse
# from ollama_llama.commands import greet, add
from ollama_llama.commands import embed, ask

# def embed():
#     print("Embedding process started...")

# def ask(question):
#     print(f"Processing question: {question}")

def main_cli():
    # Create the main parser
    parser = argparse.ArgumentParser(prog="ollama_llama", description="Ollama LLaMA command-line interface")
    
    # Add subcommands
    subparsers = parser.add_subparsers(dest="command", help="Subcommands")

    # Subcommand: embed
    parser_embed = subparsers.add_parser("embed", help="Embed content using Ollama LLaMA")
    
    # Subcommand: ask
    parser_ask = subparsers.add_parser("ask", help="Ask a question using Ollama LLaMA")
    parser_ask.add_argument("question", type=str, help="The question to ask")

    args = parser.parse_args()

    # Call the appropriate function based on the subcommand
    if args.command == "embed":
        embed.run()
    elif args.command == "ask":
        ask.run(args.question)
    else:
        parser.print_help()  # Show help if no valid subcommand is provided
    


    