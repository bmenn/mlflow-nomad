"""
mlflow-nomad: A MLflow project backend for Nomad

"""
__version__ = "0.1.0"

from mlflow.projects.backend.abstract_backend import AbstractBackend
from mlflow.projects.submitted_run import SubmittedRun


class NomadProvider(AbstractBackend):
    """
    Abstract plugin class defining the interface needed to execute MLflow projects. You can define
    subclasses of ``AbstractBackend`` and expose them as third-party plugins to enable running
    MLflow projects against custom execution backends (e.g. to run projects against your team's
    in-house cluster or job scheduler). See `MLflow Plugins <../../plugins.html>`_ for more
    information.
    """

    def run(self, project_uri, entry_point, params,
            version, backend_config, tracking_uri, experiment_id):
        """
        Submit an entrypoint. It must return a SubmittedRun object to track the execution

        :param project_uri: URI of the project to execute, e.g. a local filesystem path
               or a Git repository URI like https://github.com/mlflow/mlflow-example
        :param entry_point: Entry point to run within the project.
        :param params: Dict of parameters to pass to the entry point
        :param version: For git-based projects, either a commit hash or a branch name.
        :param backend_config: A dictionary, or a path to a JSON file (must end in '.json'), which
                               will be passed as config to the backend. The exact content which
                               should be provided is different for each execution backend and is
                               documented at https://www.mlflow.org/docs/latest/projects.html.
        :param tracking_uri: URI of tracking server against which to log run information related
                             to project execution.
        :param experiment_id: ID of experiment under which to launch the run.

        :return: A :py:class:`mlflow.projects.SubmittedRun`. This function is expected to run
                 the project asynchronously, i.e. it should trigger project execution and then
                 immediately return a `SubmittedRun` to track execution status.
        """
        raise NotImplementedError()
        nomad_server = nomad.Nomad(host=backend_config['server'])
        # Jobspec items to include:
        #   .group[].task[].resources.{cpu,memory,device}
        #   .group[].task[].config.image
        #   .group[].task[].volume_mount
        #   .group[].volume
        # TODO Nomad client needs to provide host_volume for shared drive
        # TODO Return a NomadSubmittedRun
        # from mlflow.projects import kubernetes as kb
        # tracking.MlflowClient().set_tag(active_run.info.run_id, MLFLOW_PROJECT_ENV, "docker")
        # tracking.MlflowClient().set_tag(active_run.info.run_id, MLFLOW_PROJECT_BACKEND,
        #                                 "kubernetes")
        # _validate_docker_env(project)
        # _validate_docker_installation()
        # kube_config = _parse_kubernetes_config(backend_config)
        # image = _build_docker_image(work_dir=work_dir,
        #                             repository_uri=kube_config["repository-uri"],
        #                             base_image=project.docker_env.get('image'),
        #                             run_id=active_run.info.run_id)
        # image_digest = kb.push_image_to_registry(image.tags[0])
        # submitted_run = kb.run_kubernetes_job(
        #     project.name,
        #     active_run,
        #     image.tags[0],
        #     image_digest,
        #     _get_entry_point_command(project, entry_point, parameters, storage_dir),
        #     _get_run_env_vars(
        #         run_id=active_run.info.run_uuid,
        #         experiment_id=active_run.info.experiment_id
        #     ),
        #     kube_config.get('kube-context', None),
        #     kube_config['kube-job-template']
        # )
        # return submitted_run


class NomadSubmittedRun(SubmittedRun):
    """Instance of SubmittedRun corresponding to a Nomad Job launched to run
    an MLflow project.

    """
    pass
