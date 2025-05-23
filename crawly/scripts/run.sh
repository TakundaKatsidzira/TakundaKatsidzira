#!/bin/bash
set -e

cd "$(dirname "$0")/.."

ROOT_URL="https://raw.githubusercontent.com/TakundaKatsidzira/TakundaKatsidzira/main/crawly/example/node0.txt"
REPORT_FILE="data/analysis_report.txt"
VERBOSE=true

echo "🚀 Starting Crawly..."
echo "🌐 Root URL: $ROOT_URL"
echo "📝 Report will be saved to: $REPORT_FILE"
echo ""

if $VERBOSE; then
  python3 -m src.crawly "$ROOT_URL" --report "$REPORT_FILE" --verbose
else
  python3 -m src.crawly "$ROOT_URL" --report "$REPORT_FILE"
fi

echo ""
echo "✅ Done. Analysis report available at: $REPORT_FILE"
