from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import errno
import os
import pickle
import six
import torch

__all__ = ['init_model', 'save_model']

def _mkdir_if_not_exist(path, logger):
    """
    mkdir if not exists, ignore the exception when multiprocess mkdir together
    """
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except OSError as e:
            if e.errno == errno.EEXIST and os.path.isdir(path):
                logger.warning(
                    'be happy if some process has already created {}'.format(
                        path))
            else:
                raise OSError('Failed to mkdir {}'.format(path))

def save_model(model,
               epoch,
               optimizer,
               scheduler,
               model_path,
               logger,
               is_best=False,
               prefix='accOCR'):
    """
    save model to the target path
    """
    epoch = 000 # 覆蓋掉
    _mkdir_if_not_exist(model_path, logger)
    save_path = os.path.join(model_path, f"Epoch_{epoch}_"+ prefix + ".pth")

    # torch.save({
    #     'model_state_dict': model.state_dict(),
    #     'optimizer_state_dict': optimizer.state_dict(),
    #     'scheduler_state_dict': scheduler.state_dict()
    # }, save_path)

    #->  Unexpected key(s) in state_dict: "epoch", "model_state_dict", "optimizer_state_dict", "scheduler_state_dict".'''
    torch.save(model.state_dict(), save_path)

    # save metric and config
    if is_best:
        logger.info('save best model is to {}'.format(model_path))
    else:
        logger.info("save model in {}".format(model_path))


'''
def save_model(epoch, model, optimizer, scheduler, model_path,logger):
    _mkdir_if_not_exist(model_path, logger)
    save_path = os.path.join(model_path, f"model_epoch_{epoch}.pth")
    torch.save({
        'epoch': epoch,
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'scheduler_state_dict': scheduler.state_dict()
    }, save_path)
    print(f"Model saved to {save_path}")
'''