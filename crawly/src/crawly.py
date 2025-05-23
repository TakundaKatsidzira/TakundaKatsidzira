import argparse
import sys
from .graph_builder import GraphBuilder
from .analyzer import Analyzer
from .report_generator import ReportGenerator

def parse_args():
    parser = argparse.ArgumentParser(description="Crawly - Hyperlinked Text Graph Analyzer")
    parser.add_argument("root_url", nargs="?", help="Root URL to start crawling")
    parser.add_argument("--report", default="data/analysis_report.txt", help="Output report file")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    return parser

def main():
    parser = parse_args()
    args = parser.parse_args()


    if not args.root_url:
        parser.print_help(sys.stdout)  # 👈 print to stdout
        sys.exit(0)

    if args.verbose:
        print(f"[INFO] Starting crawl at: {args.root_url}")

    builder = GraphBuilder()
    graph, dead_links = builder.build_graph(args.root_url)

    if args.verbose:
        print(f"[INFO] Graph built with {len(graph)} nodes")

    analyzer = Analyzer(graph, dead_links)
    analysis_results = analyzer.analyze()

    if args.verbose:
        analyzer.print_bfs_layers(args.root_url)

    report = ReportGenerator()
    report.generate(analysis_results, args.report)

    if args.verbose:
        print(f"[INFO] Report saved to {args.report}")

if __name__ == "__main__":
    main()
