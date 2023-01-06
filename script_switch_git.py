import os

base_path = '/Users/albuquerquehenrique'
git_path = '.gitconfig'
work_path = '.bcg_gitconfig'
personal_path = '.personal_gitconfig'


def main():
    if (os.path.exists('/Users/albuquerquehenrique/'+work_path)):
        print('Switched to work git account')
        os.rename('/Users/albuquerquehenrique/'+git_path,
                  '/Users/albuquerquehenrique/'+personal_path)
        os.rename('/Users/albuquerquehenrique/'+work_path,
                  '/Users/albuquerquehenrique/'+git_path)
        return

    if (os.path.exists('/Users/albuquerquehenrique/'+personal_path)):
        print('Switched to personal git account')
        os.rename('/Users/albuquerquehenrique/'+git_path,
                  '/Users/albuquerquehenrique/'+work_path)
        os.rename('/Users/albuquerquehenrique/'+personal_path,
                  '/Users/albuquerquehenrique/'+git_path)
        return


main()
