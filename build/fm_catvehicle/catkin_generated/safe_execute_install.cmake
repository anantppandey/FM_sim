execute_process(COMMAND "/home/anant/FM_sim/build/fm_catvehicle/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/anant/FM_sim/build/fm_catvehicle/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
