This component generates a list of numbers that can be used as the number of buildings story in an urban district to reach the desired urban density.

---

### Inputs:
- `buildings_number`: The number of buildings in the district
- `start_floor_range`: Minimum buildings story
- `end_floor_range`: Maximum buildings story
- `density`: Desired urban district density
- `fprints_area`: List of buildings' footprint areas. *note that the order of this list is corresponding to the* `best_floors_match` *list*.
- `iterations`: The number loops that the component iterates over to find the best matches. *note that increasing the number of this input makes the calculation slower and the solutions more accurate*.
- `recompute`: Connect a "Boolean Toggle" to this input to recompute calculations.

### Outputs:
- `best_floors_match`: The list of numbers that can use as the number of buildings story.
- `result_densities`: The list of calculated densities to find the best match. This list has a similar length as the `iterations` number.
- `best_seed`: The seed of the best match. Record it if you want to recreate the same composition later.
- `best_iter_index`: The index of best iteration in the list of all iterations.
- `best_match_density`: Check this number, it should be slightly different from the input number. If not, `recompute` the component.



*Notice that the code is optimized for densities higher than 2 and less than 14. If you are working with higher densities, some changes in code may require; or just increase the value of* `start_floor_range` :)
