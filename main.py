import argparse
from datetime import datetime
import signal
from search import (
    EightPuzzle,
    breadth_first_graph_search,
    astar_search,
    iterative_deepening_search,
)
from utils import (
    parse_text_file,
    print_puzzle,
    manhattan,
    max_heuristic,
    rev_map,
)


def solve(problem, algo, res_dict):

    start_time = datetime.now()
    if algo == "BFS":
        solution = breadth_first_graph_search(problem)
    elif algo == "IDS":
        solution = iterative_deepening_search(problem)
    elif algo == "h1":
        solution = astar_search(problem)
    elif algo == "h2":
        solution = astar_search(problem, h=manhattan)
    elif algo == "h3":
        solution = astar_search(problem, h=max_heuristic)
    end_time = datetime.now()

    time = end_time - start_time

    res = {
        "nodes": problem.nodes_generated,
        "time": time.total_seconds(),
    }

    if not res_dict:
        print(f"Total nodes generated: {problem.nodes_generated}")
        print(f"Total time taken:, {time.seconds} sec {time.microseconds} microSec")
        print(f"Path length: {len(solution.solution())}")
        print("A valid sequence of actions:", "".join(rev_map(solution.solution())))

    return res


def handler(signum, frame):
    print("Total nodes generated: <<??>>")
    print("Total time taken: >15 min")
    print("Path length: Timed out.")
    print("Path: Timed out.")
    exit()


def run(fpath, alg, res_dict):

    # Parse puzzle as tuple
    initial_state = parse_text_file(fpath)

    # Create problem object
    problem = EightPuzzle(initial_state)

    # print_puzzle(initial_state)

    if problem.check_solvability(initial_state) is False:
        print("The inputted puzzle is not solvable:")
        print_puzzle(initial_state)
        return

    signal.signal(signal.SIGALRM, handler)
    signal.alarm(15 * 60)

    res = solve(problem, alg, res_dict)

    return res


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Run 8puz solver",
    )

    parser.add_argument("--fPath", required=True, help="Path to file")
    parser.add_argument("--alg", required=True, help="Algorithm to use")
    parser.add_argument(
        "--res_dict",
        required=False,
        default=0,
        type=int,
        help="Returns nodes generated and time",
    )

    args = parser.parse_args()

    if args.alg not in ["BFS", "IDS", "h1", "h2", "h3"]:
        print("Invalid algorithm, please choose from [BFS, IDS, h1, h2, h3]")
        exit()

    run(fpath=args.fPath, alg=args.alg, res_dict=args.res_dict)
