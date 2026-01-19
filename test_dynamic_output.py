"""
TEST: Prove that output changes with different data
This script runs the same workflow with 3 different scenarios and shows different results
"""

import asyncio
from orchestrator import AgenticOrchestrator
import json


async def test_scenario_1():
    """Scenario 1: Minor emergency"""
    print("\n" + "="*70)
    print("TEST 1: MINOR EMERGENCY - Small population, low severity")
    print("="*70)

    scenario = {
        "data_source": {
            "source_type": "text",
            "data": """
            EMERGENCY REPORT - Minor Flood

            Region X (Population: 100,000):
            - 10% power outage
            - All hospitals operational
            - Emergency shelters: 5 operational
            - Supplies: Water (90% stock), Medical (95% stock)
            - Road access: 95% operational

            Available Resources:
            - Medical teams: 5 teams
            - Budget: $5 Million
            """
        },
        "context": "Minor flood, low urgency",
        "objectives": ["Ensure safety", "Minimize disruption"],
        "options": [
            {"option_id": "1", "name": "Monitor and wait", "description": "Keep watch, deploy if needed"},
            {"option_id": "2", "name": "Light response", "description": "Send 1-2 teams"}
        ],
        "constraints": {"budget": "$5M", "time": "48 hours"},
        "resources": {"teams": "5"},
        "timeline": "48 hours"
    }

    orchestrator = AgenticOrchestrator()
    result = await orchestrator.execute_workflow(scenario, verbose=False)

    decision = result['stages']['decision'].data.get('decision', {})
    print("\n🤖 AI DECISION:")
    print(f"Recommendation: {decision.get('RECOMMENDED DECISION', decision.get('decision_summary', 'N/A'))}")
    print(f"Confidence: {decision.get('CONFIDENCE LEVEL', decision.get('confidence', 'N/A'))}")
    print(f"Priority: {decision.get('IMPLEMENTATION PRIORITY', 'N/A')}")

    return result


async def test_scenario_2():
    """Scenario 2: Critical emergency"""
    print("\n" + "="*70)
    print("TEST 2: CRITICAL EMERGENCY - Large population, high severity")
    print("="*70)

    scenario = {
        "data_source": {
            "source_type": "text",
            "data": """
            EMERGENCY REPORT - Major Earthquake

            Region Y (Population: 5,000,000):
            - 95% power outage
            - 8 of 10 hospitals collapsed
            - Emergency shelters: 2 operational, 30 damaged
            - Supplies: Water (5% stock), Medical (10% stock)
            - Road access: 30% operational
            - Casualties: 5,000 injured, 1,000 missing

            Available Resources:
            - Medical teams: 20 teams
            - Budget: $100 Million
            """
        },
        "context": "Major earthquake, CRITICAL urgency, lives at stake",
        "objectives": ["Save lives immediately", "Prevent further casualties", "Rapid response"],
        "options": [
            {"option_id": "1", "name": "Full deployment", "description": "Deploy ALL resources immediately"},
            {"option_id": "2", "name": "Staged response", "description": "Deploy in waves"}
        ],
        "constraints": {"budget": "$100M", "time": "6 hours"},
        "resources": {"teams": "20"},
        "timeline": "24 hours"
    }

    orchestrator = AgenticOrchestrator()
    result = await orchestrator.execute_workflow(scenario, verbose=False)

    decision = result['stages']['decision'].data.get('decision', {})
    print("\n🤖 AI DECISION:")
    print(f"Recommendation: {decision.get('RECOMMENDED DECISION', decision.get('decision_summary', 'N/A'))}")
    print(f"Confidence: {decision.get('CONFIDENCE LEVEL', decision.get('confidence', 'N/A'))}")
    print(f"Priority: {decision.get('IMPLEMENTATION PRIORITY', 'N/A')}")

    return result


async def test_scenario_3():
    """Scenario 3: Economic decision (completely different domain)"""
    print("\n" + "="*70)
    print("TEST 3: ECONOMIC POLICY - Completely different domain")
    print("="*70)

    scenario = {
        "data_source": {
            "source_type": "text",
            "data": """
            ECONOMIC ANALYSIS REPORT

            Current Situation:
            - Inflation: 8%
            - Unemployment: 4%
            - GDP Growth: 2%
            - National Debt: $30 Trillion
            - Consumer Confidence: Low

            Problem: Rising costs affecting middle class
            """
        },
        "context": "Economic policy decision to combat inflation",
        "objectives": ["Reduce inflation", "Maintain employment", "Support middle class"],
        "options": [
            {"option_id": "1", "name": "Raise interest rates", "description": "Federal Reserve increases rates to 5%"},
            {"option_id": "2", "name": "Stimulus package", "description": "Provide tax relief to middle class"}
        ],
        "constraints": {"political": "Election year", "economic": "Recession risk"},
        "resources": {"budget": "$2 Trillion"},
        "timeline": "1 year"
    }

    orchestrator = AgenticOrchestrator()
    result = await orchestrator.execute_workflow(scenario, verbose=False)

    decision = result['stages']['decision'].data.get('decision', {})
    print("\n🤖 AI DECISION:")
    print(f"Recommendation: {decision.get('RECOMMENDED DECISION', decision.get('decision_summary', 'N/A'))}")
    print(f"Confidence: {decision.get('CONFIDENCE LEVEL', decision.get('confidence', 'N/A'))}")
    print(f"Priority: {decision.get('IMPLEMENTATION PRIORITY', 'N/A')}")

    return result


async def main():
    print("\n" + "🧪"*35)
    print("TESTING: Does the AI generate different outputs for different data?")
    print("🧪"*35)

    # Run all 3 tests
    result1 = await test_scenario_1()
    result2 = await test_scenario_2()
    result3 = await test_scenario_3()

    # Compare decisions
    print("\n" + "="*70)
    print("📊 COMPARISON OF RESULTS")
    print("="*70)

    decision1 = result1['stages']['decision'].data.get('decision', {}).get('RECOMMENDED DECISION', 'N/A')
    decision2 = result2['stages']['decision'].data.get('decision', {}).get('RECOMMENDED DECISION', 'N/A')
    decision3 = result3['stages']['decision'].data.get('decision', {}).get('RECOMMENDED DECISION', 'N/A')

    print(f"\nTest 1 (Minor Flood):  {decision1[:100]}...")
    print(f"\nTest 2 (Earthquake):   {decision2[:100]}...")
    print(f"\nTest 3 (Economic):     {decision3[:100]}...")

    if decision1 == decision2 == decision3:
        print("\n❌ FAIL: All decisions are identical (hardcoded)")
    else:
        print("\n✅ PASS: Decisions are different (AI-generated)")
        print("\nCONCLUSION: The output is DYNAMIC and changes based on input data!")

    print("\n" + "="*70)


if __name__ == "__main__":
    print("\n⚠️  This test will take 2-3 minutes (3 AI analyses)")
    print("Press Ctrl+C to cancel, or wait to see results...\n")

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\nTest cancelled by user")
