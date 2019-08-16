# heap_pop function returns the first element of the list implementing the heap, 
# providing the heap is not empty
def heap_pop(heap):
    if heap != []:
        vertex,weight,parent = heap.pop(0)
        return (vertex, weight, parent)
    else:
        raise

example_triplet_heap=[
    ((1,1),2,(1,0)),
    ((1,2),4,(0,2)),
    ((2,1),18,(2,0))
]

(vertex, distance, parent) = heap_pop(example_triplet_heap)

print("The element of the heap of minimum distance contains as vertex: {}, as distance: {}, and as parent: {}"
.format(vertex,distance,parent))
