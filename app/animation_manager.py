from matplotlib import pyplot as plt, animation
from app.sorting_algorithms import Sorting_Algorithms

class Animation_Manager:
    def __init__(self, k_digits = 1, data = []):
        self._sorting_algorithms = Sorting_Algorithms()
        self._k_digits = k_digits
        self._data = data
        self._data_size = len(data) + 1

    def visualize_bubble_sort(self):
        data = self._data.copy()
        generator = self._sorting_algorithms.bubble_sort(data)

        fig, ax = plt.subplots()
        ax.set_title("Bubble Sort O(n\N{SUPERSCRIPT TWO})")
        bar_sub = ax.bar(range(len(self._data)), self._data, align="edge")

        ax.set_xlim(0, self._data_size)
        text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
        iteration = [0]

        def update(data, rects, iteration):
            if data['is_sorting_done'] is False:
                for rect, val in zip(rects, data['list']):
                    rect.set_height(val)
                iteration[0] += 1
                text.set_text(f"# of operations: {iteration[0]}")
            else: # when bubble sort is done
                index = 0
                for rect, val in zip(rects, data['list']):
                    if index >= (self._data_size - 1) - self._k_digits:
                        rect.set(color='green') # change the kth top digits bar color to green
                    index += 1

        anim = animation.FuncAnimation(
        fig,
        func=update,
        fargs=(bar_sub, iteration),
        frames=generator,
        repeat=False,
        blit=False,
        interval=15,
        save_count=90000,
        )

        plt.show()
        plt.close()

    def visualize_quick_sort(self):
        data = self._data.copy()
        generator = self._sorting_algorithms.quicksort(data, 0, len(data)-1, self._k_digits)

        fig, ax = plt.subplots()
        ax.set_title("Quick Sort O(n)")
        bar_sub = ax.bar(range(len(self._data)), self._data, align="edge")

        ax.set_xlim(0, self._data_size)
        text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
        iteration = [0]

        def update(data, rects, iteration):
            if data['is_sorting_done'] is False:
                index = 0
                for rect, val in zip(rects, data['list']):
                    if data['finish_index'] is not None and index >= data['finish_index'][0] and index <= data['finish_index'][1]:
                        rect.set(color='red')
                    
                    rect.set_height(val)
                    index += 1
                    
                iteration[0] += 1
                text.set_text(f"# of operations: {iteration[0]}")
            else: # when bubble sort is done
                index = 0
                for rect, val in zip(rects, data['list']):
                    if index < self._k_digits:
                        rect.set(color='green') # change the kth top digits bar color to green
                    else:
                        rect.set(color='red')
                    index += 1

        anim = animation.FuncAnimation(
        fig,
        func=update,
        fargs=(bar_sub, iteration),
        frames=generator,
        repeat=False,
        blit=False,
        interval=15,
        save_count=90000,
        )

        plt.show()
        plt.close()