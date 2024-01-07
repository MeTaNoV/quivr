import { AxiosInstance } from "axios";

export const createApiKey = async (
  axiosInstance: AxiosInstance
): Promise<string> => {
  const response = await axiosInstance.post<{ api_key: string }>("/api-key");

  return response.data.api_key;
};

// TODO(pg): finish this
export const listApiKeys = async (axiosInstance: AxiosInstance): Promise<string[]> => {
  const response = await axiosInstance.get<string[]>("/api-key");

  return response.data;
}

export const deleteApiKey = async (axiosInstance: AxiosInstance) => {
  const response = await axiosInstance.delete("/api-key");

  return response.data;
}