import subprocess

def analyze_case(amount):
    try:
        prompt = f"""
You are an expert debt collection AI.

Overdue amount: ₹{amount}

Classify priority as LOW, MEDIUM, or HIGH.
Explain the reason clearly in 3 lines.
"""

        result = subprocess.run(
            ["ollama", "run", "llama3"],
            input=prompt,
            text=True,
            capture_output=True,
            timeout=30
        )

        if result.returncode != 0:
            return {"error": result.stderr}

        return {
            "priority": "AI Generated",
            "reason": result.stdout.strip()
        }

    except Exception as e:
        return {"error": str(e)}
