# Simulates Snowflake metrics output as Prometheus-style metrics

import random
import time

warehouses = ['analytics_wh', 'etl_wh', 'bi_wh']

while True:
    for warehouse in warehouses:
        credits_used = round(random.uniform(10.0, 100.0), 2)
        print(f'snowflake_credits_used{{warehouse="{warehouse}"}} {credits_used}')
    time.sleep(0.5)
