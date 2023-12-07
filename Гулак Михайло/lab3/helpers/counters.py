from classes import (
    BasicContainer,
    HeavyContainer,
    RefrigeratedContainer,
    LiquidContainer,
)


def count_containers_by_type(containers, container_type) -> int:
    count = 0

    for container in containers:
        if not isinstance(container, container_type):
            continue

        count += 1

    return count


def count_containers(containers) -> map:
    count = {
        "basic": count_containers_by_type(containers, BasicContainer),
        "heavy": count_containers_by_type(containers, HeavyContainer),
        "refrigerated": count_containers_by_type(containers, RefrigeratedContainer),
        "liquid": count_containers_by_type(containers, LiquidContainer),
    }

    return count
