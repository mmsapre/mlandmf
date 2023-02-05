import numpy as np

def projection(u,v):
    v_norm = np.sqrt(sum(v ** 2))
    proj_of_u_on_v = (np.dot(u, v) / v_norm ** 2) * v
    return proj_of_u_on_v

def main():
    printopt = np.get_printoptions()
    np.set_printoptions(formatter={'float': '{:8.3g}'.format}, linewidth=200)
    u = np.array([1, 2, 3])
    v = np.array([5, 6, 2])
    proj=projection(u,v)
    print('projection = \n{}'.format(proj))

if __name__ == '__main__':
    main()