import pygame
import unittest
from main import Groob

class TestGroob(unittest.TestCase):
    def setUp(self):
        pygame.init()
        # Set up a test display
        self.test_screen = pygame.display.set_mode((500, 500))
        self.groob = Groob()
        
    def test_initial_state(self):
        """Test initial state of Groob"""
        self.assertEqual(self.groob.state, 'idle')
        self.assertEqual(self.groob.x_velo, 0)
        self.assertEqual(self.groob.y_velo, 0)
        self.assertFalse(self.groob.onGround)
        
    def test_movement(self):
        """Test basic movement mechanics"""
        initial_x = self.groob.rect.x
        
        # Test moving right
        keys = {pygame.K_d: True, pygame.K_a: False, pygame.K_SPACE: False}
        self.groob.update(keys, 5, 500, 500)
        self.assertTrue(self.groob.rect.x > initial_x)
        self.assertEqual(self.groob.state, 'walking')
        
        # Test moving left
        keys = {pygame.K_d: False, pygame.K_a: True, pygame.K_SPACE: False}
        initial_x = self.groob.rect.x
        self.groob.update(keys, 5, 500, 500)
        self.assertTrue(self.groob.rect.x < initial_x)
        self.assertEqual(self.groob.state, 'walking')
        
    def test_gravity(self):
        """Test gravity and jumping mechanics"""
        # Place Groob in air
        self.groob.rect.y = 200
        self.groob.onGround = False
        initial_y = self.groob.rect.y
        
        # Test falling
        keys = {pygame.K_d: False, pygame.K_a: False, pygame.K_SPACE: False}
        self.groob.update(keys, 5, 500, 500)
        self.assertTrue(self.groob.rect.y > initial_y)
        
        # Test jumping
        self.groob.onGround = True
        keys = {pygame.K_d: False, pygame.K_a: False, pygame.K_SPACE: True}
        initial_y_velo = self.groob.y_velo
        self.groob.update(keys, 5, 500, 500)
        self.assertTrue(self.groob.y_velo < initial_y_velo)
        self.assertFalse(self.groob.onGround)
        
    def test_boundaries(self):
        """Test screen boundary collisions"""
        # Test right boundary
        self.groob.rect.x = 490
        keys = {pygame.K_d: True, pygame.K_a: False, pygame.K_SPACE: False}
        self.groob.update(keys, 5, 500, 500)
        self.assertEqual(self.groob.rect.right, 500)
        
        # Test left boundary
        self.groob.rect.x = 5
        keys = {pygame.K_d: False, pygame.K_a: True, pygame.K_SPACE: False}
        self.groob.update(keys, 5, 500, 500)
        self.assertEqual(self.groob.rect.left, 0)
        
        # Test bottom boundary
        self.groob.rect.y = 490
        self.groob.update(keys, 5, 500, 500)
        self.assertEqual(self.groob.rect.bottom, 500)
        self.assertTrue(self.groob.onGround)
        
    def test_animation_state(self):
        """Test animation state changes"""
        # Test idle state
        keys = {pygame.K_d: False, pygame.K_a: False, pygame.K_SPACE: False}
        self.groob.update(keys, 5, 500, 500)
        self.assertEqual(self.groob.state, 'idle')
        
        # Test walking state
        keys = {pygame.K_d: True, pygame.K_a: False, pygame.K_SPACE: False}
        self.groob.update(keys, 5, 500, 500)
        self.assertEqual(self.groob.state, 'walking')
        
    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main() 