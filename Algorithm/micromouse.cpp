#include "micromouse.h"

Micromouse::Micromouse() {
    // Constructor implementation if needed
}

void Micromouse::navigateToCenter() {
    int startX = 0, startY = 0;
    auto path = bfs(startX, startY);

    // Move the micromouse along the found path
    for (auto& step : path) {
        // Implement movement based on the path
        // For simplicity, assume just moving forward
        api.moveForward();
    }
}

bool Micromouse::isValidMove(int x, int y) {
    // Implement logic to check if the move is valid
    // Check bounds and walls using API calls
    return (x >= 0 && x < api.mazeWidth() &&
            y >= 0 && y < api.mazeHeight() &&
            !api.wallFront()); // Example check for wall in front
}

bool Micromouse::isCenter(int x, int y) {
    // Implement logic to check if the micromouse is at the center
    int centerX = api.mazeWidth() / 2;
    int centerY = api.mazeHeight() / 2;
    return (x == centerX && y == centerY);
}

void Micromouse::moveForward() {
    // Implement logic to move the micromouse forward using API
    api.moveForward();
}

void Micromouse::turnRight() {
    // Implement logic to turn the micromouse right using API
    api.turnRight();
}

void Micromouse::turnLeft() {
    // Implement logic to turn the micromouse left using API
    api.turnLeft();
}

void Micromouse::backtrack() {
    // Implement logic to backtrack if necessary
    // Example: Turn around 180 degrees and move back
    api.turnRight();
    api.turnRight();
    api.moveForward();
    // Additional logic as needed
}

std::vector<std::pair<int, int>> Micromouse::bfs(int startX, int startY) {
    std::queue<Cell> q;
    std::unordered_set<int> visited; // Using hash set for visited cells
    q.push({startX, startY, {}}); // Start with initial position and empty path
    visited.insert(startX * api.mazeWidth() + startY); // Mark starting cell as visited

    while (!q.empty()) {
        Cell current = q.front();
        q.pop();

        // Check if we've reached the center
        if (isCenter(current.x, current.y)) {
            return current.path;
        }

        // Explore in all four directions
        for (int i = 0; i < 4; ++i) {
            int newX = current.x + (i == 0 ? 1 : i == 2 ? -1 : 0); // Move in x direction
            int newY = current.y + (i == 1 ? 1 : i == 3 ? -1 : 0); // Move in y direction

            if (isValidMove(newX, newY)) {
                // Mark cell as visited
                int hashVal = newX * api.mazeWidth() + newY;
                if (visited.find(hashVal) == visited.end()) {
                    visited.insert(hashVal);
                    // Create a new path vector and add current cell's path to it
                    std::vector<std::pair<int, int>> newPath = current.path;
                    newPath.push_back({newX, newY});
                    // Enqueue the new cell with updated path
                    q.push({newX, newY, newPath});
                }
            }
        }
    }

    return {}; // Return empty path if no path found
}
