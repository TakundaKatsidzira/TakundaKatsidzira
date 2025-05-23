#!/bin/bash

# Default root URL (you can change this to your preferred starting file)
ROOT_URL="https://raw.githubusercontent.com/TakundaKatsidzira/TakundaKatsidzira/main/crawly/example/root.txt"


# Default report output location
REPORT_FILE="data/analysis_report.txt"

# Verbosity flag
VERBOSE=true

echo "🚀 Starting Crawly..."
echo "🌐 Root URL: $ROOT_URL"
echo "📝 Report will be saved to: $REPORT_FILE"
echo ""

# Activate virtual environment if exists (optional)
# source venv/bin/activate

# Run the Python script
if $VERBOSE; then
  python3 src/crawly.py "$ROOT_URL" --report "$REPORT_FILE" --verbose
else
  python3 src/crawly.py "$ROOT_URL" --report "$REPORT_FILE"
fi

echo ""
echo "✅ Done. Analysis report available at: $REPORT_FILE"
