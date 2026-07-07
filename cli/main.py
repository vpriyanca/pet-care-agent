import argparse
from agents.pet_session_agent import PetSessionAgent

def main():
    parser = argparse.ArgumentParser(description="Pet Companion Agent CLI")
    parser.add_argument("command", help="Command: daily, feed, groom, play, exercise, mood")
    parser.add_argument("--behavior", help="Behavior description for mood detection", default="")

    args = parser.parse_args()
    agent = PetSessionAgent()

    if args.command == "daily":
        agent.start_daily_routine()

    elif args.command == "feed":
        agent.run_feeding()

    elif args.command == "groom":
        agent.run_grooming()

    elif args.command == "play":
        agent.run_play()

    elif args.command == "exercise":
        agent.run_exercise()

    elif args.command == "mood":
        if not args.behavior:
            print("Please provide --behavior, e.g.: --behavior restless")
        else:
            agent.check_mood(args.behavior)

    else:
        print("Unknown command. Use: daily, feed, groom, play, exercise, mood")

if __name__ == "__main__":
    main()
