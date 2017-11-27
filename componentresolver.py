class ComponentResolver:
    def __init__(self, kpicture):
        self.base = kpicture
        self.components_by_color = {}
        
        ungrouped_pixels = set([(x, y) for x in range(self.base.dimx) for y in range(self.base.dimy)])
        
        while len(ungrouped_pixels):
            pixelx, pixely = next(iter(ungrouped_pixels))
            component = Component(self.base, pixelx, pixely)
            if component.color in self.components_by_color:
                self.components_by_color[component.color].append(component)
            else:
                self.components_by_color[component.color] = [component]
            ungrouped_pixels = ungrouped_pixels.difference(component.elements)
            
