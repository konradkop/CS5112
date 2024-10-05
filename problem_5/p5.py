def cookies_distrubution_map(apartments) -> list:
    num_apartments = len(apartments)

    # If there are no apartments, return an empty list
    if num_apartments == 0:
        return []

    # Define the starting apartment position (starting_point)
    starting_point = ((num_apartments + 1) // 2, (num_apartments + 1) // 2)

    # Sets for tracking unvisited and visited apartments
    unvisited_apartments = set(apartments)
    visited_apartments = {starting_point}  # Start with the starting apartment
    mst_edges = []  # List to store the minimum spanning tree edges

    # While there are unvisited apartments
    while unvisited_apartments:
        shortest_distance = float('inf')
        closest_visited, closest_unvisited = None, None

        # Check distances from each visited apartment to all unvisited apartments
        for visited in visited_apartments:
            for unvisited in unvisited_apartments:
                # Calculate Manhattan distance
                distance = abs(visited[0] - unvisited[0]) + abs(visited[1] - unvisited[1])
                
                # Update if a closer apartment is found
                if distance < shortest_distance:
                    shortest_distance = distance
                    closest_visited = visited
                    closest_unvisited = unvisited

        # If we found a closest apartment, add it to the MST
        if closest_visited and closest_unvisited:
            mst_edges.append((closest_visited, closest_unvisited))  # Append the edge to the MST
            visited_apartments.add(closest_unvisited)  # Mark this apartment as visited
            unvisited_apartments.remove(closest_unvisited)  # Remove it from the unvisited set

    return mst_edges  # Return the list of edges in the minimum spanning tree
