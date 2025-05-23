# coding: utf-8

"""
    Control-M Services

    Provides access to BMC Control-M Services  # noqa: E501

    OpenAPI spec version: 9.21.340
    Contact: customer_support@bmc.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Job(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'duration': 'int',
        'run_as': 'str',
        'archive_rule': 'str',
        'job_id': 'str',
        'folder_id': 'str',
        'number_of_runs': 'int',
        'name': 'str',
        'folder': 'str',
        'type': 'str',
        'status': 'str',
        'held': 'bool',
        'deleted': 'bool',
        'cyclic': 'bool',
        'start_time': 'str',
        'end_time': 'str',
        'estimated_start_time': 'list[str]',
        'estimated_end_time': 'list[str]',
        'order_date': 'str',
        'ctm': 'str',
        'description': 'str',
        'host': 'str',
        'library': 'str',
        'application': 'str',
        'sub_application': 'str',
        'job_json': 'str',
        'output_uri': 'str',
        'log_uri': 'str'
    }

    attribute_map = {
        'duration': 'duration',
        'run_as': 'runAs',
        'archive_rule': 'archiveRule',
        'job_id': 'jobId',
        'folder_id': 'folderId',
        'number_of_runs': 'numberOfRuns',
        'name': 'name',
        'folder': 'folder',
        'type': 'type',
        'status': 'status',
        'held': 'held',
        'deleted': 'deleted',
        'cyclic': 'cyclic',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'estimated_start_time': 'estimatedStartTime',
        'estimated_end_time': 'estimatedEndTime',
        'order_date': 'orderDate',
        'ctm': 'ctm',
        'description': 'description',
        'host': 'host',
        'library': 'library',
        'application': 'application',
        'sub_application': 'subApplication',
        'job_json': 'jobJSON',
        'output_uri': 'outputURI',
        'log_uri': 'logURI'
    }

    def __init__(self, duration=None, run_as=None, archive_rule=None, job_id=None, folder_id=None, number_of_runs=None, name=None, folder=None, type=None, status=None, held=None, deleted=None, cyclic=None, start_time=None, end_time=None, estimated_start_time=None, estimated_end_time=None, order_date=None, ctm=None, description=None, host=None, library=None, application=None, sub_application=None, job_json=None, output_uri=None, log_uri=None):  # noqa: E501
        """Job - a model defined in Swagger"""  # noqa: E501
        self._duration = None
        self._run_as = None
        self._archive_rule = None
        self._job_id = None
        self._folder_id = None
        self._number_of_runs = None
        self._name = None
        self._folder = None
        self._type = None
        self._status = None
        self._held = None
        self._deleted = None
        self._cyclic = None
        self._start_time = None
        self._end_time = None
        self._estimated_start_time = None
        self._estimated_end_time = None
        self._order_date = None
        self._ctm = None
        self._description = None
        self._host = None
        self._library = None
        self._application = None
        self._sub_application = None
        self._job_json = None
        self._output_uri = None
        self._log_uri = None
        self.discriminator = None
        if duration is not None:
            self.duration = duration
        if run_as is not None:
            self.run_as = run_as
        if archive_rule is not None:
            self.archive_rule = archive_rule
        if job_id is not None:
            self.job_id = job_id
        if folder_id is not None:
            self.folder_id = folder_id
        if number_of_runs is not None:
            self.number_of_runs = number_of_runs
        if name is not None:
            self.name = name
        if folder is not None:
            self.folder = folder
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if held is not None:
            self.held = held
        if deleted is not None:
            self.deleted = deleted
        if cyclic is not None:
            self.cyclic = cyclic
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if estimated_start_time is not None:
            self.estimated_start_time = estimated_start_time
        if estimated_end_time is not None:
            self.estimated_end_time = estimated_end_time
        if order_date is not None:
            self.order_date = order_date
        if ctm is not None:
            self.ctm = ctm
        if description is not None:
            self.description = description
        if host is not None:
            self.host = host
        if library is not None:
            self.library = library
        if application is not None:
            self.application = application
        if sub_application is not None:
            self.sub_application = sub_application
        if job_json is not None:
            self.job_json = job_json
        if output_uri is not None:
            self.output_uri = output_uri
        if log_uri is not None:
            self.log_uri = log_uri

    @property
    def duration(self):
        """Gets the duration of this Job.  # noqa: E501


        :return: The duration of this Job.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Job.


        :param duration: The duration of this Job.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def run_as(self):
        """Gets the run_as of this Job.  # noqa: E501


        :return: The run_as of this Job.  # noqa: E501
        :rtype: str
        """
        return self._run_as

    @run_as.setter
    def run_as(self, run_as):
        """Sets the run_as of this Job.


        :param run_as: The run_as of this Job.  # noqa: E501
        :type: str
        """

        self._run_as = run_as

    @property
    def archive_rule(self):
        """Gets the archive_rule of this Job.  # noqa: E501


        :return: The archive_rule of this Job.  # noqa: E501
        :rtype: str
        """
        return self._archive_rule

    @archive_rule.setter
    def archive_rule(self, archive_rule):
        """Sets the archive_rule of this Job.


        :param archive_rule: The archive_rule of this Job.  # noqa: E501
        :type: str
        """

        self._archive_rule = archive_rule

    @property
    def job_id(self):
        """Gets the job_id of this Job.  # noqa: E501

        Order ID of the job.  # noqa: E501

        :return: The job_id of this Job.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this Job.

        Order ID of the job.  # noqa: E501

        :param job_id: The job_id of this Job.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def folder_id(self):
        """Gets the folder_id of this Job.  # noqa: E501

        Order ID of the folder containing this job.  # noqa: E501

        :return: The folder_id of this Job.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this Job.

        Order ID of the folder containing this job.  # noqa: E501

        :param folder_id: The folder_id of this Job.  # noqa: E501
        :type: str
        """

        self._folder_id = folder_id

    @property
    def number_of_runs(self):
        """Gets the number_of_runs of this Job.  # noqa: E501

        The run number (in case of cyclic jobs or reruns)  # noqa: E501

        :return: The number_of_runs of this Job.  # noqa: E501
        :rtype: int
        """
        return self._number_of_runs

    @number_of_runs.setter
    def number_of_runs(self, number_of_runs):
        """Sets the number_of_runs of this Job.

        The run number (in case of cyclic jobs or reruns)  # noqa: E501

        :param number_of_runs: The number_of_runs of this Job.  # noqa: E501
        :type: int
        """

        self._number_of_runs = number_of_runs

    @property
    def name(self):
        """Gets the name of this Job.  # noqa: E501

        The name of the run job.  # noqa: E501

        :return: The name of this Job.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Job.

        The name of the run job.  # noqa: E501

        :param name: The name of this Job.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def folder(self):
        """Gets the folder of this Job.  # noqa: E501

        The name of the run job.  # noqa: E501

        :return: The folder of this Job.  # noqa: E501
        :rtype: str
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """Sets the folder of this Job.

        The name of the run job.  # noqa: E501

        :param folder: The folder of this Job.  # noqa: E501
        :type: str
        """

        self._folder = folder

    @property
    def type(self):
        """Gets the type of this Job.  # noqa: E501

        The type of the run job.  # noqa: E501

        :return: The type of this Job.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Job.

        The type of the run job.  # noqa: E501

        :param type: The type of this Job.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def status(self):
        """Gets the status of this Job.  # noqa: E501

        The status of the run job.  # noqa: E501

        :return: The status of this Job.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Job.

        The status of the run job.  # noqa: E501

        :param status: The status of this Job.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def held(self):
        """Gets the held of this Job.  # noqa: E501

        Is job held.  # noqa: E501

        :return: The held of this Job.  # noqa: E501
        :rtype: bool
        """
        return self._held

    @held.setter
    def held(self, held):
        """Sets the held of this Job.

        Is job held.  # noqa: E501

        :param held: The held of this Job.  # noqa: E501
        :type: bool
        """

        self._held = held

    @property
    def deleted(self):
        """Gets the deleted of this Job.  # noqa: E501

        Is job held.  # noqa: E501

        :return: The deleted of this Job.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Job.

        Is job held.  # noqa: E501

        :param deleted: The deleted of this Job.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def cyclic(self):
        """Gets the cyclic of this Job.  # noqa: E501

        Is it a cyclic job.  # noqa: E501

        :return: The cyclic of this Job.  # noqa: E501
        :rtype: bool
        """
        return self._cyclic

    @cyclic.setter
    def cyclic(self, cyclic):
        """Sets the cyclic of this Job.

        Is it a cyclic job.  # noqa: E501

        :param cyclic: The cyclic of this Job.  # noqa: E501
        :type: bool
        """

        self._cyclic = cyclic

    @property
    def start_time(self):
        """Gets the start_time of this Job.  # noqa: E501

        The start time of the job run.  # noqa: E501

        :return: The start_time of this Job.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Job.

        The start time of the job run.  # noqa: E501

        :param start_time: The start_time of this Job.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this Job.  # noqa: E501

        The end time of the job run.  # noqa: E501

        :return: The end_time of this Job.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Job.

        The end time of the job run.  # noqa: E501

        :param end_time: The end_time of this Job.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def estimated_start_time(self):
        """Gets the estimated_start_time of this Job.  # noqa: E501

        The estimated start time of the jobs.  # noqa: E501

        :return: The estimated_start_time of this Job.  # noqa: E501
        :rtype: list[str]
        """
        return self._estimated_start_time

    @estimated_start_time.setter
    def estimated_start_time(self, estimated_start_time):
        """Sets the estimated_start_time of this Job.

        The estimated start time of the jobs.  # noqa: E501

        :param estimated_start_time: The estimated_start_time of this Job.  # noqa: E501
        :type: list[str]
        """

        self._estimated_start_time = estimated_start_time

    @property
    def estimated_end_time(self):
        """Gets the estimated_end_time of this Job.  # noqa: E501

        The estimated end time of the jobs.  # noqa: E501

        :return: The estimated_end_time of this Job.  # noqa: E501
        :rtype: list[str]
        """
        return self._estimated_end_time

    @estimated_end_time.setter
    def estimated_end_time(self, estimated_end_time):
        """Sets the estimated_end_time of this Job.

        The estimated end time of the jobs.  # noqa: E501

        :param estimated_end_time: The estimated_end_time of this Job.  # noqa: E501
        :type: list[str]
        """

        self._estimated_end_time = estimated_end_time

    @property
    def order_date(self):
        """Gets the order_date of this Job.  # noqa: E501

        The order date.  # noqa: E501

        :return: The order_date of this Job.  # noqa: E501
        :rtype: str
        """
        return self._order_date

    @order_date.setter
    def order_date(self, order_date):
        """Sets the order_date of this Job.

        The order date.  # noqa: E501

        :param order_date: The order_date of this Job.  # noqa: E501
        :type: str
        """

        self._order_date = order_date

    @property
    def ctm(self):
        """Gets the ctm of this Job.  # noqa: E501

        The controlm server.  # noqa: E501

        :return: The ctm of this Job.  # noqa: E501
        :rtype: str
        """
        return self._ctm

    @ctm.setter
    def ctm(self, ctm):
        """Sets the ctm of this Job.

        The controlm server.  # noqa: E501

        :param ctm: The ctm of this Job.  # noqa: E501
        :type: str
        """

        self._ctm = ctm

    @property
    def description(self):
        """Gets the description of this Job.  # noqa: E501

        The job description.  # noqa: E501

        :return: The description of this Job.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Job.

        The job description.  # noqa: E501

        :param description: The description of this Job.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def host(self):
        """Gets the host of this Job.  # noqa: E501

        host machine where the job runs.  # noqa: E501

        :return: The host of this Job.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this Job.

        host machine where the job runs.  # noqa: E501

        :param host: The host of this Job.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def library(self):
        """Gets the library of this Job.  # noqa: E501

        The folder library.  # noqa: E501

        :return: The library of this Job.  # noqa: E501
        :rtype: str
        """
        return self._library

    @library.setter
    def library(self, library):
        """Sets the library of this Job.

        The folder library.  # noqa: E501

        :param library: The library of this Job.  # noqa: E501
        :type: str
        """

        self._library = library

    @property
    def application(self):
        """Gets the application of this Job.  # noqa: E501

        job application.  # noqa: E501

        :return: The application of this Job.  # noqa: E501
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this Job.

        job application.  # noqa: E501

        :param application: The application of this Job.  # noqa: E501
        :type: str
        """

        self._application = application

    @property
    def sub_application(self):
        """Gets the sub_application of this Job.  # noqa: E501

        job subApplication.  # noqa: E501

        :return: The sub_application of this Job.  # noqa: E501
        :rtype: str
        """
        return self._sub_application

    @sub_application.setter
    def sub_application(self, sub_application):
        """Sets the sub_application of this Job.

        job subApplication.  # noqa: E501

        :param sub_application: The sub_application of this Job.  # noqa: E501
        :type: str
        """

        self._sub_application = sub_application

    @property
    def job_json(self):
        """Gets the job_json of this Job.  # noqa: E501

        The JSON string that describes the job.  # noqa: E501

        :return: The job_json of this Job.  # noqa: E501
        :rtype: str
        """
        return self._job_json

    @job_json.setter
    def job_json(self, job_json):
        """Sets the job_json of this Job.

        The JSON string that describes the job.  # noqa: E501

        :param job_json: The job_json of this Job.  # noqa: E501
        :type: str
        """

        self._job_json = job_json

    @property
    def output_uri(self):
        """Gets the output_uri of this Job.  # noqa: E501

        A URI that can be used to get the output of the run job  # noqa: E501

        :return: The output_uri of this Job.  # noqa: E501
        :rtype: str
        """
        return self._output_uri

    @output_uri.setter
    def output_uri(self, output_uri):
        """Sets the output_uri of this Job.

        A URI that can be used to get the output of the run job  # noqa: E501

        :param output_uri: The output_uri of this Job.  # noqa: E501
        :type: str
        """

        self._output_uri = output_uri

    @property
    def log_uri(self):
        """Gets the log_uri of this Job.  # noqa: E501

        A URI that can be used to get the log of the run job  # noqa: E501

        :return: The log_uri of this Job.  # noqa: E501
        :rtype: str
        """
        return self._log_uri

    @log_uri.setter
    def log_uri(self, log_uri):
        """Sets the log_uri of this Job.

        A URI that can be used to get the log of the run job  # noqa: E501

        :param log_uri: The log_uri of this Job.  # noqa: E501
        :type: str
        """

        self._log_uri = log_uri

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Job, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Job):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
