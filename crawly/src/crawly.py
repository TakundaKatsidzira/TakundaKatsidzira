import argparse
import sys
from .graph_builder import GraphBuilder
from .analyzer import Analyzer
from .report_generator import ReportGenerator
from .utils import normalize_url

def parse_args():
    parser = argparse.ArgumentParser(description="Crawly - Hyperlinked Text Graph Analyzer")
    parser.add_argument("root_url", help="Root URL to start crawling from")
    parser.add_argument("--report", default="data/analysis_report.txt", help="Output report file")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    return parser.parse_args()

def main():
    args = parse_args()
    root_url = normalize_url(args.root_url)

    if args.verbose:
        print(f"[INFO] Starting crawl at: {root_url}")

    # Build graph
    builder = GraphBuilder(verbose=args.verbose)
    graph, dead_links = builder.build_graph(root_url)

    if args.verbose:
        print(f"[INFO] Graph built: {len(graph)} nodes, {len(dead_links)} dead links")

    # Analyze graph
    analyzer = Analyzer(graph, dead_links, verbose=args.verbose)
    results = analyzer.analyze()

    # Optional BFS hierarchy output
    if args.verbose:
        analyzer.print_bfs_layers(root_url)

    # Generate report
    report = ReportGenerator()
    report.generate(results, args.report)

    if args.verbose:
        print(f"[INFO] Report saved to: {args.report}")

if __name__ == "__main__":
    main()
