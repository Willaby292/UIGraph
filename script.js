class Node {
    constructor(x, y) {
        this.x = x;
        this.y = y;
        this.neighbors = {
            'UP': null,
            'DOWN': null,
            'LEFT': null,
            'RIGHT': null
        };
        this.element = this.createElement();
    }

    createElement() {
        const div = document.createElement('div');
        div.classList.add('circle');
        div.style.left = this.x + 'px';
        div.style.top = this.y + 'px';
        document.getElementById('circle-container').appendChild(div);
        return div;
    }

    setNeighbor(node, direction) {
        this.neighbors[direction] = node;
        this.updateColor();
    }

    updateColor(color = 'blue') {
        this.element.style.backgroundColor = color;
    }
}

class Graph {
    constructor(nodes) {
        this.nodes = nodes;
        this.currentNode = this.nodes[0];
        this.currentNode.updateColor('red');
    }

    move(direction) {
        const nextNode = this.currentNode.neighbors[direction];
        if (nextNode) {
            this.currentNode.updateColor();
            this.currentNode = nextNode;
            this.currentNode.updateColor('red');
        }
    }
}

function createRandomPOI(screenWidth, screenHeight) {
    const nodeRadius = 15;
    const navbarHeight = document.querySelector('.navbar').offsetHeight;
    const buttonContainerHeight = document.querySelector('.button-container').offsetHeight;
    const maxX = screenWidth - 2 * nodeRadius;
    const minX = 2 * nodeRadius;
    const maxY = screenHeight - navbarHeight - 2 * nodeRadius;
    const minY = 2 * nodeRadius

    const nodes = [];
    for (let i = 0; i < 20; i++) { // Number of nodes
        const x = Math.floor(Math.random() * (maxX - minX) + minX);
        const y = Math.floor(Math.random() * (maxY - minY) + minY);
        nodes.push(new Node(x, y));
    }
    return nodes;
}

function findNeighborsHeatMap(nodes) {
    nodes.forEach(currNode => {
        let minMatchValue = { 'UP': Infinity, 'DOWN': Infinity, 'LEFT': Infinity, 'RIGHT': Infinity };

        nodes.forEach(node => {
            if (node === currNode) return;

            const dx = node.x - currNode.x;
            const dy = node.y - currNode.y;
            const matchValue = Math.abs(dx) + Math.abs(dy);

            if (dy <= dx && dy <=-dx) {
                if (matchValue < minMatchValue['UP']) {
                    currNode.setNeighbor(node, 'UP');
                    minMatchValue['UP'] = matchValue;
                }
            } else if (dy >= dx && dy >=-dx)  {
                if (matchValue < minMatchValue['DOWN']) {
                    currNode.setNeighbor(node, 'DOWN');
                    minMatchValue['DOWN'] = matchValue;
                }
            } else if (dy >= dx && dy <=-dx) {
                if (matchValue < minMatchValue['LEFT']) {
                    currNode.setNeighbor(node, 'LEFT');
                    minMatchValue['LEFT'] = matchValue;
                }
            } else if (dy <= dx && dy >=-dx) {
                if (matchValue < minMatchValue['RIGHT']) {
                    currNode.setNeighbor(node, 'RIGHT');
                    minMatchValue['RIGHT'] = matchValue;
                }
            }
        });
    });
}

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM fully loaded and parsed');

    let graph = null;

    document.getElementById('generate-poi-btn').addEventListener('click', function() {
        const screenWidth = window.innerWidth;
        const screenHeight = window.innerHeight;

        // Clear existing nodes
        const circleContainer = document.getElementById('circle-container');
        circleContainer.innerHTML = '';

        const nodes = createRandomPOI(screenWidth, screenHeight);
        findNeighborsHeatMap(nodes);

        // Initialize graph with new nodes
        graph = new Graph(nodes);
    });

    document.addEventListener('keydown', function(event) {
        if (graph) {
            switch (event.key) {
                case 'ArrowUp':
                    graph.move('UP');
                    break;
                case 'ArrowDown':
                    graph.move('DOWN');
                    break;
                case 'ArrowLeft':
                    graph.move('LEFT');
                    break;
                case 'ArrowRight':
                    graph.move('RIGHT');
                    break;
            }
        }
    });
});
