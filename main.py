
from agent.planner import plan_next_action
from agent.executor import execute_action
from agent.memory import load_memory, save_memory

def main():
    goal = input("🌐 What should I do? ")
    session_id = "default"
    memory = load_memory(session_id)
    context = {"goal": goal, "memory": memory}

    while True:
        action = plan_next_action(context)
        print(f"\n🧠 Agent decided: {action['description']}")
        result = execute_action(action)
        context['memory'].append((action, result))
        save_memory(session_id, context['memory'])

        if action.get("type") == "done":
            break

if __name__ == "__main__":
    main()
