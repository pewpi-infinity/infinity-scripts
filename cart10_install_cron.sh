#!/bin/sh
CRON_LINE="0 * * * * cd $HOME/infinity-scripts && ./cart08_pipeline_run.sh >> pipeline.log 2>&1"

(crontab -l 2>/dev/null | grep -v cart08_pipeline_run.sh; echo "$CRON_LINE") | crontab -
echo "Cron installed: hourly mining research run"
