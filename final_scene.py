#Created by Nicolò Candiani

from manim import *

class HorseShoe(Scene):
    def construct(self):
        #number of iterations
        n_iteration = 1
        
        #create square containing the invariant set
        square = Square() 
        
        # generate forward iteration rectangles
        f_rect_1 = self.create_points([-1,1,0],[-0.20,1,0], [-0.20, -1, 0], [-1,-1,0], 1000)
        f_rect_1.set_fill(GREEN, opacity=0.5)
        
        f_rect_2 = self.create_points([0.2,1,0],[1,1,0], [1, -1, 0], [0.2,-1,0], 1000)
        f_rect_2.set_fill(RED, opacity=0.5)
        
        f_rect_3 = self.create_points([-0.2, 1, 0], [0.20, 1, 0], [0.20, -1, 0], [-0.2, -1, 0], 1000)
        f_rect_3.set_fill(PURPLE, opacity=0.5)
        
        #create group of forward rectangles
        f_rects = Group(f_rect_1, f_rect_2, f_rect_3)
        f_rects.generate_points()
        
        #create map iteration counter
        decimal = Integer(0).move_to([-6,3,0])
        tracker = ValueTracker(i)
        decimal.add_updater(lambda d: d.set_value(tracker.get_value()))
        tracker.set_value(0)
        
        #adding counter, rectangles and square on screen
        self.add(decimal)
        self.add(square, f_rects)
        self.wait(2)
        
        #updating counter since we are starting the first iteration of the map 
        tracker.set_value(1)
        #play forward iteration
        #stretching of the rectangles
        self.play(
                ApplyMatrix(self.f_stretching(), f_rects, about_point=np.array([-1,-1,0]))
            )
        #folding and translation of the rectangles
        self.play(
                ApplyPointwiseFunction(self.f_map_to_circle, f_rects)
            )

        self.wait()
        
        #generating backward iteration rectangles
        b_rect_1 = self.create_points([1,-1, 0],[1, -0.20, 0], [-1, -0.20, 0], [-1,-1,0], 1000)
        b_rect_1.set_fill(GREEN, opacity=0.5)
        
        b_rect_2 = self.create_points([1,1,0],[1,0.2,0],[-1,0.2,0],[-1,1, 0], 1000)
        b_rect_2.set_fill(RED, opacity=0.5)
        
        b_rect_3 = self.create_points([1, -0.2, 0], [1,0.2, 0], [-1,0.2, 0], [-1, -0.2, 0], 1000)
        b_rect_3.set_fill(PURPLE, opacity=0.5)
        
        #creating backward iteration group of rectangles
        b_rects = Group(b_rect_1, b_rect_2, b_rect_3)
        b_rects.generate_points()
        
       #display backward iteration group       
        self.add(b_rects)
        self.wait(2)
        
        #play backward iteration
        #stretching of the rectangles
        self.play(
                ApplyMatrix(self.b_stretching(), b_rects, about_point=np.array([-1,-1,0])),
            )
        #folding and translation  
        self.play(
                ApplyPointwiseFunction(self.b_map_to_circle, b_rects),
        )

        self.wait()
        
        i = 1
        # start iteration loop to show more iterations faster
        while i < n_iteration:
            # update iteration counter
            tracker.set_value(int(i+1))
            #playing forward and backward stretching
            self.play(
                ApplyMatrix(self.f_stretching(), f_rects, about_point=np.array([-1,-1,0])),
                ApplyMatrix(self.b_stretching(), b_rects, about_point=np.array([-1,-1,0])),
            )
            
            #stretching and folding of rectangles
            self.play(
                ApplyPointwiseFunction(self.f_map_to_circle, f_rects),
                ApplyPointwiseFunction(self.b_map_to_circle, b_rects),
            )

            self.wait()
            i+=1
        
    
    
    def create_points(self, a, b, c, d, n):
        '''
        Creates a 4 sided polygon with an arbitrary amount of points n along each side connecting two corners.
        """
        Parameters
        ----------
        a : list
            position of corner 1
        b : list
            position of corner 2
        c : list
            position of corner 3
        d : list
            position of corner 4
        n: int
            number of points to be calculated along each side
        
        Returns
        -------
        Polygon
            polygon with n points between each corner. stroke_width is set to 0 by default.
        '''
        points = []
        for e in np.linspace(a,b,n):
            points.append(e.tolist())
        for e in np.linspace(b,c,n):
            points.append(e.tolist())
        for e in np.linspace(c,d,n):
            points.append(e.tolist())
        for e in np.linspace(d,a,n):
            points.append(e.tolist())
            
        return Polygon(*points, color=WHITE, stroke_width=0)
    
    def f_map_to_circle(self, p):
        '''
        Second transformation of the forward iteration, mapping a part of the rectangles to a circle and translating the other

        Parameters
        ----------
        p : list
            3 dimensional point
        
        Returns
        -------
        list
            new point obtained by applying the mapping
        '''
        
        x,y,z = p
        #mapping to circle
        if x >= 1 and x < 2:
            #move to the origin for the mapping to the circle
            x = x-1
            new_x = (-np.sin(np.pi*x)*y) + 1
            new_y = (np.cos(np.pi*x)*y)
            return [new_x, new_y,z]
        #translation 
        if x >= 2:
            x = x
            y = y
            #moving to right place
            new_x = (-x) + 3
            new_y = (-y)
            return [new_x, new_y,z]
        return [x,y,z]
    
    def f_stretching(self):
        '''
        First transformation of the forward iteration
        
        Returns
        -------
        matrix
            2x2 matrix stretching a point along the x axis
        '''
        return [[2.5,0],[0, 0.4]]
    
    def b_map_to_circle(self, p): 
        '''
        Second transformation of the backward iteration, mapping a part of the rectangles to a circle and translating the other

        Parameters
        ----------
        p : list
            3 dimensional point
        
        Returns
        -------
        list
            new point obtained by applying the mapping
        '''
        #inverting x and y to keep code from forward function
        y,x,z = p
        if x >= 1 and x < 2:
            x = x-1
            new_x = (-np.sin(np.pi*x)*y) + 1
            new_y = (np.cos(np.pi*x)*y)
            #need to return x and y swapped too
            return [new_y,new_x,z]
        if x >= 2:
            x = x
            y = y
            new_x = (-x) + 3
            new_y = (-y)
            #same x and y swapping here
            return [new_y, new_x,z]
        return [y,x,z]
        
    def b_stretching(self):
        '''
        First transformation of the backward iteration
        
        Returns
        -------
        matrix
            2x2 matrix stretching a point along the y axis
        '''
        return [[0.4,0],[0, 2.5]]