from component import *

class ComponentResolver:
    def __init__(self, kpicture, border_thickness = 10):
        self.base = kpicture
        self.base.add_border(border_thickness, color = -1)
        
        
        ungrouped_pixels = set([(x, y) for x in range(self.base.dimx) for y in range(self.base.dimy)])
       
        # Make main stencil component
        self.stencil_component = Component(self.base, startx = 0, starty = 0)
        ungrouped_pixels = ungrouped_pixels.difference(self.stencil_component.elements)
       
        
        # Find remaining components
        self.components = []
         
        while len(ungrouped_pixels):
            startx, starty = next(iter(ungrouped_pixels))
            component = Component(self.base, startx, starty)
            self.components.append(component)
            ungrouped_pixels = ungrouped_pixels.difference(component.elements)
        
    def simplify(self, threshold = 0):
        if not threshold:
            threshold = (self.base.dimx * self.base.dimy)**(1/8)
        changed = True
        while changed:
            changed = False
            for component in self.components[:]:
                if len(component.elements) < threshold:
                    changed = True
                    for other in self.components[:]:
                        if other.adj(component):
                            other.merge(component)
                            self.components.remove(component)
                            break
                
        
    def next_boundary_color(self):
        for component in self.components:
            if component.adj(self.stencil_component):
                return component.color
    
    def num_components(self):
        return len(self.components)
    
    def grow(self):
        color = self.next_boundary_color()
        for component in self.components[:]:
            if component.color == color and self.stencil_component.adj(component):
                self.stencil_component.merge(component)
                self.components.remove(component)
