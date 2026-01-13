import matplotlib.pyplot as plt
from pathlib import Path

# Find project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

 
def plot_pareto(F, pareto_F):
    plt.figure()
    plt.scatter(F[:, 0], F[:, 1], alpha=0.3, label="All Solutions")
    plt.scatter(pareto_F[:, 0], pareto_F[:, 1], color="red", label="Pareto Front")
    plt.xlabel("Throughput")
    plt.ylabel("Defect")
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "pareto_front.png")
    plt.close()


def plot_knee_point(pareto_F, knee_point):
    plt.figure()
    plt.scatter(pareto_F[:, 0], pareto_F[:, 1])
    plt.scatter(knee_point[0], knee_point[1], marker="X", s=120, color="red")
    plt.xlabel("Throughput")
    plt.ylabel("Defect")
    plt.title("Knee Point")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "knee_point.png")
    plt.close()


def plot_weighted_sum(pareto_F, ws_solutions):
    plt.figure()
    plt.scatter(pareto_F[:, 0], pareto_F[:, 1], label="Pareto Front")
    plt.scatter(ws_solutions[:, 0], ws_solutions[:, 1],
                color="green", label="Weighted Sum Solutions")
    plt.legend()
    plt.xlabel("Throughput")
    plt.ylabel("Defect")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "weighted_sum_isolines.png")
    plt.close()


def plot_epsilon_constraint(pareto_F, eps_solutions):
    plt.figure()
    plt.scatter(pareto_F[:, 0], pareto_F[:, 1], label="Pareto Front")
    plt.scatter(eps_solutions[:, 0], eps_solutions[:, 1],
                color="purple", label="Epsilon Constraint Solutions")
    plt.legend()
    plt.xlabel("Throughput")
    plt.ylabel("Defect")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "epsilon_constraint.png")
    plt.close()
