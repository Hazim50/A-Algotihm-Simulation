<h1>A* Pathfinding Algorithm Simulation</h1>

<p>This project implements a visualization of the A* pathfinding algorithm using Pygame. A* is a popular graph traversal and path search algorithm, often used in various fields such as robotics and video games.</p>

<h2>Table of Contents</h2>

<ul>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#how-to-use">How to Use</a></li>
    <li><a href="#dependencies">Dependencies</a></li>
    <li><a href="#license">License</a></li>
</ul>

<h2>Introduction</h2>

<p>The A* algorithm efficiently finds the shortest path between two points in a graph. It works by iteratively selecting the most promising node to explore next based on a heuristic function that estimates the cost to reach the goal from that node.</p>

<p>This project consists of Python scripts that collectively simulate the A* algorithm in action, allowing users to interactively create mazes, place start and end points, and observe the algorithm finding the shortest path through the maze.</p>

<h2>Project Structure</h2>

<p>The project comprises the following Python scripts:</p>

<ul>
    <li><strong>a_star.py:</strong> Contains the implementation of the A* algorithm.</li>
    <li><strong>create_maze.py:</strong> Generates random mazes based on given parameters.</li>
    <li><strong>draw_maze.py:</strong> Handles the visualization of the maze and algorithm using Pygame.</li>
    <li><strong>events.py:</strong> Manages user events such as mouse clicks and keyboard inputs.</li>
    <li><strong>main.py:</strong> Initializes the game and orchestrates the interaction between different components.</li>
</ul>

<h2>How to Use</h2>

<p>To run the A* algorithm simulation:</p>

<ol>
    <li>Ensure you have Python installed on your system.</li>
    <li>Install the Pygame library if not already installed: <code>pip install pygame</code>.</li>
    <li>Clone this repository to your local machine.</li>
    <li>Navigate to the project directory.</li>
    <li>Run the <code>main.py</code> script using Python: <code>python main.py</code>.</li>
    <li>Follow the on-screen instructions to create mazes, set start and end points, and observe the algorithm's execution.</li>
</ol>

<h2>Dependencies</h2>

<ul>
    <li>Python 3.x</li>
    <li>Pygame</li>
</ul>
