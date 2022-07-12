import sys, os, functools
from inspect import getframeinfo, stack
import log


def paiplog(_func=None):
    def log_decorator_info(func):
        py_file_caller = getframeinfo(stack()[2][0])
        # print("====================")
        # print(py_file_caller.function)
        # print("====================")
        if py_file_caller.function != "<module>" : 
            @functools.wraps(func)
            def log_decorator_wrapper(self, *args, **kwargs):
                # Build logger object
                logger_obj = log.get_logger(log_file_name='.'.join(py_file_caller.filename.split('.')[:-1]), log_sub_dir='.')# log_sub_dir='.'.join(py_file_caller.filename.split('.')[:-1]))

                args_passed_in_function = [repr(a) for a in args]
                kwargs_passed_in_function = [f"{k}={v!r}" for k, v in kwargs.items()]

                formatted_arguments = ", ".join(args_passed_in_function + kwargs_passed_in_function)
                
                extra_args = { 'func_name_override': func.__name__,'file_name_override': os.path.basename(py_file_caller.function) }
                logger_obj.info(f"Arguments: {formatted_arguments} - Begin function")
                try:
                    """ log return value from the function """
                    value = func(self, *args, **kwargs)
                    logger_obj.info(f"Returned: - End function {value!r}",extra=extra_args)
                except:
                    """log exception if occurs in function"""
                    logger_obj.error(f"Exception: {str(sys.exc_info()[1])}",extra=extra_args)
                    raise
                # Return function value
                return value
            # Return the pointer to the function
            return log_decorator_wrapper

        else : 
            @functools.wraps(func)
            def log_decorator_wrapper(*args, **kwargs):
                # Build logger object
                logger_obj = log.get_logger(log_file_name='.'.join(py_file_caller.filename.split('.')[:-1]), log_sub_dir='')

                args_passed_in_function = [repr(a) for a in args]
                kwargs_passed_in_function = [f"{k}={v!r}" for k, v in kwargs.items()]

                formatted_arguments = ", ".join(args_passed_in_function + kwargs_passed_in_function)
                
                extra_args = { 'func_name_override': func.__name__,'file_name_override': os.path.basename(py_file_caller.filename) }
                logger_obj.info(f"Arguments: {formatted_arguments} - Begin function")
                try:
                    """ log return value from the function """
                    value = func(*args, **kwargs)
                    logger_obj.info(f"Returned: - End function {value!r}",extra=extra_args)
                except:
                    """log exception if occurs in function"""
                    logger_obj.error(f"Exception: {str(sys.exc_info()[1])}",extra=extra_args)
                    raise
                # Return function value
                return value
            # Return the pointer to the function
            return log_decorator_wrapper

    # Decorator was called with arguments, so return a decorator function that can read and return a function
    if _func is None:
        return log_decorator_info
    # Decorator was called without arguments, so apply the decorator to the function immediately
    else:
        return log_decorator_info(_func)

