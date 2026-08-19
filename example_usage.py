from client import AgentTaskEvaluationBenchmarkHarnessSynthesizerClient

def main():
    client = AgentTaskEvaluationBenchmarkHarnessSynthesizerClient()
    res = client.evaluate_agent_benchmark("Multi-hop SQL Tool Invocation", 12)
    print(f"Pass Rate: {res['benchmark_pass_rate_pct']}%")
    print(f"Scenarios: {res['scenarios_evaluated']}")
    print(f"Summary: {res['evaluation_summary']}")

if __name__ == "__main__":
    main()
