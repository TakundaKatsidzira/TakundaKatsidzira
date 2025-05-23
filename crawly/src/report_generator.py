class ReportGenerator:
    def generate(self, results, output_file):
        try:
            with open(output_file, 'w') as f:
                f.write("==== Crawly Analysis Report ====\n\n")
                
                f.write(f"Total Nodes: {results['total_nodes']}\n")
                f.write(f"Dead Links: {len(results['dead_links'])}\n")
                f.write(f"Leaf Nodes: {len(results['leaf_nodes'])}\n")
                f.write(f"Cycles Detected: {'Yes' if results['has_cycles'] else 'No'}\n\n")

                f.write("Top Frequent Files:\n")
                for url, freq in results['top_frequent']:
                    f.write(f"  - {url} ({freq} visits)\n")
                f.write("\n")

                f.write("Top Files by Size:\n")
                for url, size in results['top_size']:
                    readable_size = self._format_size(size)
                    f.write(f"  - {url} ({readable_size})\n")
                f.write("\n")

                f.write("Topological Sort (Dependency Order):\n")
                for url in results['topo_sort']:
                    f.write(f"  - {url}\n")
                f.write("\n")

        except Exception as e:
            print(f"❌ Error writing report to {output_file}: {e}")

    def _format_size(self, size_bytes):
        for unit in ['bytes', 'KB', 'MB', 'GB']:
            if size_bytes < 1024:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.1f} TB"
