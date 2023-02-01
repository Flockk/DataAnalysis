def can_build(milestones, new_cafe_count, max_dist):
    built = 0
    last = 0
    for i in range(len(milestones)):
        while (milestones[i] - last > max_dist) and (built <= new_cafe_count):
            built += 1
            last += max_dist
        last = milestones[i]
    return built <= new_cafe_count


road_length, new_cafe_count, max_dist = map(int, input().split())
milestone_count = int(input())
milestones = list(map(int, input().split()))
milestones.append(road_length)
milestones.sort()

print("YES" if can_build(milestones, new_cafe_count, max_dist) else "NO")
