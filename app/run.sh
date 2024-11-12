#!/bin/bash

# 1. ない場合は自動で環境作成
# 2. プログラム実行 

# SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

DATE_TO_USE=$(date +"%Y%m%d")
# -p オプションがあれば、その日付を使用
while getopts "p:" opt; do
    case $opt in
        p) DATE_TO_USE=$OPTARG ;;
    esac
done

WORK_DIR="src/work/$DATE_TO_USE"

if [ ! -d "$WORK_DIR" ]; then
    echo "Creating new directory: $WORK_DIR"
    mkdir -p "$WORK_DIR"
    touch "$WORK_DIR/main.py"

    # cat > "$WORK_DIR/main.py" << 'EOF'
    # EOF
    echo "Created new main.py"
fi

RYE_CMD="rye run python3 $WORK_DIR/main.py"
echo "Running: $RYE_CMD"
$RYE_CMD