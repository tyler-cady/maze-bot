#ifndef MICROMOUSE_H
#define MICROMOUSE_H

#include <vector>
#include <queue>
#include <utility> // For pair
#include <unordered_set>
#include "API/api.h" // Include the provided API header

class Micromouse {
public:
    Micromouse(); // Constructor
    void navigateToCenter(); // Function to navigate to the center of the maze

private:
    enum Direction { NORTH, EAST, SOUTH, WEST };

    // Helper functions
    bool isValidMove(int x, int y);
    bool isCenter(int x, int y);
    void moveForward();
    void turnRight();
    void turnLeft();
    void backtrack();
    
    // API instance
    fp::API api;

    // Define the cell structure for BFS
    struct Cell {
        int x, y;
        std::vector<std::pair<int, int>> path;
    };

    // BFS to find the shortest path to the center
    std::vector<std::pair<int, int>> bfs(int startX, int startY);
};

#endif // MICROMOUSE_H
