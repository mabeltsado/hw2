"""
User Research Synthesizer
--------------------------
Summarizes raw user research notes into structured, leadership-ready insights.

Usage:
    python app.py --input "Your raw research notes here"
    python app.py --input-file notes.txt
    python app.py --input "Notes..." --output results.md
    python app.py --input "Notes..." --system-prompt "Custom instruction..."

Requirements:
    pip install anthropic
    export ANTHROPIC_API_KEY=your_key_here
"""

import argparse
import os
import sys
from datetime import datetime
import anthropic

# ── Default system prompt (configurable via --system-prompt) ─────────────────
DEFAULT_SYSTEM_PROMPT = """You are an expert UX researcher and strategic communicator.
Your job is to synthesize raw user research notes into clear, structured insights
suitable for a leadership audience.

Always respond in the following format:

## Key Themes
- [Bullet list of 2-4 central themes from the research]

## Core User Pain Points
- [Bullet list of specific frustrations or unmet needs]

## Actionable Recommendations
- [Bullet list of 2-4 concrete opportunities or next steps for the team]

## Confidence & Caveats
[1-2 sentences noting data quality, conflicting signals, or gaps that need follow-up]

Be concise, avoid restating raw notes, and write for a VP or C-suite audience."""


def synthesize(research_notes: str, system_prompt: str, model: str) -> str:
    """Send research notes to Claude and return the synthesized summary."""
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    message = client.messages.create(
        model=model,
        max_tokens=1024,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": f"Please synthesize the following user research notes:\n\n{research_notes}"
            }
        ]
    )
    return message.content[0].text


def save_output(content: str, output_path: str, research_notes: str):
    """Save the synthesis result to a markdown file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_output = f"# User Research Synthesis\n_Generated: {timestamp}_\n\n---\n\n{content}\n\n---\n\n**Raw Input:**\n> {research_notes[:300]}{'...' if len(research_notes) > 300 else ''}\n"
    with open(output_path, "w") as f:
        f.write(full_output)
    print(f"\n[Saved to {output_path}]")


def main():
    parser = argparse.ArgumentParser(description="Synthesize user research notes into leadership insights.")

    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("--input", type=str, help="Raw research notes as a string")
    input_group.add_argument("--input-file", type=str, help="Path to a .txt file containing research notes")

    parser.add_argument("--output", type=str, default="output.md", help="Output file path (default: output.md)")
    parser.add_argument("--system-prompt", type=str, default=DEFAULT_SYSTEM_PROMPT, help="Custom system prompt for the LLM")
    parser.add_argument("--model", type=str, default="claude-3-5-haiku-20241022", help="Claude model to use")

    args = parser.parse_args()

    # ── Load input ────────────────────────────────────────────────────────────
    if args.input_file:
        if not os.path.exists(args.input_file):
            print(f"Error: File '{args.input_file}' not found.")
            sys.exit(1)
        with open(args.input_file, "r") as f:
            research_notes = f.read().strip()
    else:
        research_notes = args.input.strip()

    if not research_notes:
        print("Error: Research notes cannot be empty.")
        sys.exit(1)

    # ── Check API key ─────────────────────────────────────────────────────────
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY environment variable not set.")
        print("Run: export ANTHROPIC_API_KEY=your_key_here")
        sys.exit(1)

    # ── Run synthesis ─────────────────────────────────────────────────────────
    print(f"\nSynthesizing research notes using {args.model}...\n")
    print("=" * 60)

    result = synthesize(research_notes, args.system_prompt, args.model)

    print(result)
    print("=" * 60)

    save_output(result, args.output, research_notes)


if __name__ == "__main__":
    main()
